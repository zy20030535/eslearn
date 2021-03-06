# -*- coding: utf-8 -*-
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.calibration import calibration_curve
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator

from eslearn.utils.timer import  timer

class ModelEvaluator():
    """Model evaluation

    """
    
    def binary_evaluator(self, true_label=None, predict_label=None, predict_prob=None,
                        accuracy_kfold=None, sensitivity_kfold=None, specificity_kfold=None, AUC_kfold=None,
                        verbose=True, is_showfig=True, legend1='HC', legend2='Patients', is_savefig=False, out_name=None):
        
        """
        This function is used to evaluate performance of the binary classification model.

        Parameters:
        ----------
        true_label: 1d array with N-sample items
            Ground truth labels.

        predict_label: 1d array with N-sample items
            predicted label

        predict_prob: N-sample by N-class matrix 
            Output predict_prob of model

        accuracy_kfold: 1d array with K items
            accuracy of k-fold cross validation

        sensitivity_kfold: 1d array with K items
            sensitivity of k-fold cross validation

        specificity_kfold: 1d array with K items
            specificity of k-fold cross validation

        AUC_kfold: 1d array with K items
             AUC of k-fold cross validation

        verbose: bool
             if print performances

        is_showfig: bool
             if show figure

        legend1, legend2: str
            scatter figure legends,

        is_savefig: bool
            if save figure to local disk

        out_name: str
            output name of the figure
        """

        # reshape to one column
        true_label = np.reshape(true_label, [np.size(true_label), ])
        predict_label = np.reshape(predict_label, [np.size(predict_label), ])
        predict_prob = np.array(predict_prob)
        # Identify the separation line located at the 0 or 0.5
        if np.min(predict_prob) >= 0:
            separation_point = 0.5
        else:
            separation_point = 0
        if np.ndim(predict_prob) == 2:
            predict_prob = predict_prob[:,-1]  # Retained the positive probability

        # accurcay, specificity(recall of negative) and
        # sensitivity(recall of positive)
        accuracy = accuracy_score(true_label, predict_label)
        report = classification_report(true_label, predict_label)
        report = report.split('\n')
        specificity = report[2].strip().split(' ')
        sensitivity = report[3].strip().split(' ')
        specificity = float([spe for spe in specificity if spe != ''][2]) 
        sensitivity = float([sen for sen in sensitivity if sen != ''][2])
        # confusion_matrix matrix
        confusion_matrix_values = confusion_matrix(true_label, predict_label)

        # roc and auc
        if len(np.unique(true_label)) == 2:
            fpr, tpr, thresh = roc_curve(true_label, predict_prob)
            auc = roc_auc_score(true_label, predict_prob)
        else:
            auc = None

        # print performances
        if verbose:
            print('\naccuracy={:.2f}\n'.format(accuracy))
            print('sensitivity={:.2f}\n'.format(sensitivity))
            print('specificity={:.2f}\n'.format(specificity))
            if auc is not None:
                print('auc={:.2f}\n'.format(auc))
            else:
                print('Multi-Classification or only one class can not calculate the AUC\n')

        #%% Plot
        if is_showfig:
            fig, ax = plt.subplots(1,3, figsize=(15,5))
    
            # Plot classification 2d scatter
            decision_0 = predict_prob[true_label == 0]
            decision_1 = predict_prob[true_label == 1]
            ax[0].scatter(decision_0, np.arange(0, len(decision_0)), marker="o", linewidth=2, color='paleturquoise')
            ax[0].scatter(decision_1, np.arange(len(decision_0), len(predict_prob)), marker="*", linewidth=2, color='darkturquoise')
            # Grid and spines
            ax[0].grid(False)
            ax[0].spines['bottom'].set_position(('axes', 0))
            ax[0].spines['left'].set_position(('axes', 0))
            ax[0].spines['top'].set_linewidth(1.5)
            ax[0].spines['right'].set_linewidth(1.5)
            ax[0].spines['bottom'].set_linewidth(1.5)
            ax[0].spines['left'].set_linewidth(1.5)
            # TODO: Identify the separation line located at the 0 or 0.5
            ax[0].plot(np.zeros(10) + separation_point, np.linspace(0, len(predict_prob),10), '--', color='k', linewidth=1.5)
            if separation_point == 0.5:
                ax[0].axis([-0.05, 1.05, 0 - len(predict_prob) / 20, len(predict_prob) + len(predict_prob) / 20]) # x and y lim
            else:
                ax[0].axis([-1.05, 1.05, 0 - len(predict_prob) / 20, len(predict_prob) + len(predict_prob) / 20]) # x and y lim               
            ax[0].set_xlabel('Decision values', fontsize=15)
            ax[0].set_ylabel('Subjects', fontsize=15)
            num1, num2, num3, num4 = 0, 1.01, 3, 0
            ax[0].legend(['Discriminant line', legend1, legend2], bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4)
    
            # Plot ROC
            if auc is not None:
                auc = '{:.2f}'.format(auc)
                auc = eval(auc)
                ax[1].set_title(f'ROC Curve (AUC = {auc})', fontsize=15, fontweight='bold')
                ax[1].set_xlabel('False Positive Rate', fontsize=15)
                ax[1].set_ylabel('True Positive Rate', fontsize=15)
                ax[1].plot(fpr, tpr, marker=".", markersize=5, linewidth=2, color='darkturquoise')
                plt.tick_params(labelsize=12)
                # Grid and spines
                ax[1].grid(False)
                ax[1].spines['top'].set_linewidth(1.5)
                ax[1].spines['right'].set_linewidth(1.5)
                ax[1].spines['bottom'].set_position(('axes', 0))
                ax[1].spines['left'].set_position(('axes', 0))
                ax[1].spines['bottom'].set_linewidth(1.5)
                ax[1].spines['left'].set_linewidth(1.5)
                # Plot random line
                ax[1].plot(np.linspace(0, 1,10), np.linspace(0, 1,10), '--', color='k', linewidth=1)
    
            # Plot Bar
            if (accuracy_kfold is not None) and (sensitivity_kfold is not None) and (specificity_kfold is not None) and (AUC_kfold is not None):
                performances = [np.mean(accuracy_kfold), np.mean(sensitivity_kfold), np.mean(specificity_kfold),np.mean(AUC_kfold)]
                std = [np.std(accuracy_kfold), np.std(sensitivity_kfold), np.std(specificity_kfold), np.std(AUC_kfold)]
                ax[2].bar(np.arange(0,len(performances)), performances, yerr = std, capsize=5, linewidth=2, color='darkturquoise')
            else:
                performances = [accuracy, sensitivity, specificity, auc]
                ax[2].bar(np.arange(0, len(performances)), performances, linewidth=2, color='darkturquoise')
    
            ax[2].tick_params(labelsize=12)
            ax[2].set_title('Classification performances', fontsize=15, fontweight='bold')
            plt.xticks(np.arange(0,len(performances)), ['Accuracy', 'Sensitivity', 'Specificity', 'AUC'], fontsize=12, rotation=45)
            # Setting
            ax[2].spines['top'].set_linewidth(1.5)
            ax[2].spines['right'].set_linewidth(1.5)
            ax[2].spines['bottom'].set_linewidth(1.5)
            ax[2].spines['left'].set_linewidth(1.5)
            plt.grid(axis='y')
            y_major_locator=MultipleLocator(0.1)
            ax[2].yaxis.set_major_locator(y_major_locator)
            
            # # Plot calibration curve
            # if auc is not None:
            #     predict_prob = (predict_prob - predict_prob.min()) / (predict_prob.max() - predict_prob.min())
            #     fraction_of_positives, mean_predicted_value = calibration_curve(true_label, predict_prob, n_bins=10)
            #     ax[3].plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
            #     ax[3].plot(mean_predicted_value, fraction_of_positives, "s-")
    
            #     ax[3].set_ylabel("Fraction of positives")
            #     ax[3].set_ylim([-0.05, 1.05])
            #     # ax[3].legend(loc="lower right")
            #     ax[3].set_title('Calibration plots  (reliability curve)')
    
            # Save figure to PDF file
            plt.tight_layout()
            plt.subplots_adjust(wspace = 0.2, hspace = 0)
            if is_savefig:
                pdf = PdfPages(out_name)
                pdf.savefig()
                pdf.close()
                
                if is_showfig:
                    plt.show()

        return accuracy, sensitivity, specificity, auc

if __name__ == "__main__":
    pass