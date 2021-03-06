#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import time
from collections import Counter
import os

from eslearn.base import DataLoader
from eslearn.machine_learning.classification._base_classification import BaseClassification
from eslearn.model_evaluator import ModelEvaluator


class Classification(DataLoader, BaseClassification):
    
    def __init__(self, configuration_file):
        DataLoader.__init__(self, configuration_file)
        BaseClassification.__init__(self, location=os.path.dirname(configuration_file))

    def main_run(self):
        # Get all inputs
        self.load_data()
        self.get_all_inputs()

        # Make pipeline
        self.make_pipeline_()
        
        # Get training and test datasets        
        cv = self.method_model_evaluation_ 
        accuracy = []
        sensitivity = []
        specificity = []
        auc = []
        pred_test = []
        decision = []
        weights = []
        target_test_all = []
        for train_index, test_index in cv.split(self.features_, self.targets_):
            feature_train = self.features_[train_index, :]
            feature_test = self.features_[test_index, :]
            target_train = self.targets_[train_index]
            target_test = self.targets_[test_index]
            target_test_all.extend(target_test)

            # Resample
            imbalance_resample = self.method_unbalance_treatment_
            if imbalance_resample:
                feature_train, target_train = imbalance_resample.fit_resample(feature_train, target_train)
                print(f"After re-sampling, the sample size are: {sorted(Counter(target_train).items())}")
            
            # Fit
            self.fit_(feature_train, target_train)
            
            # Get weights
            self.get_weights_(feature_train, target_train)
            
            # Predict
            y_pred, y_prob = self.predict(feature_test)
            
            # Eval performances
            acc, sens, spec, auc_ = ModelEvaluator().binary_evaluator(
                target_test, y_pred, y_prob,
                accuracy_kfold=None, sensitivity_kfold=None, specificity_kfold=None, AUC_kfold=None,
                verbose=False, is_showfig=False, is_savefig=False
            )
            
            accuracy.append(acc)
            sensitivity.append(sens)
            specificity.append(spec)
            auc.append(auc_)
            pred_test.extend(y_pred)
            decision.extend(y_prob)
            weights.append(self.weights_)
         
        # Eval performances for all fold
        acc, sens, spec, auc = ModelEvaluator().binary_evaluator(
            target_test_all, pred_test, decision,
            accuracy_kfold=accuracy, sensitivity_kfold=sensitivity, specificity_kfold=specificity, AUC_kfold=auc,
            verbose=1, is_showfig=False, is_savefig=False, legend1='EMCI', legend2='AD', out_name=r"D:\悦影科技\数据处理业务1\data_variance_22_30_z\分类结果\adVSemci.pdf")

        return y_pred, y_prob


if __name__ == "__main__":
    time_start = time.time()
    clf = Classification(configuration_file=r'D:\My_Codes\virtualenv_eslearn\Lib\site-packages\eslearn\GUI\test\configuration_file.json') 
    clf.main_run()
    time_end = time.time()
    print(clf.param_search_)
    print(clf.pipeline_)
    print(f"Running time = {time_end-time_start}\n")
    print("="*50)