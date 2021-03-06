#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
Base class for all modules
"""

import json
import re
import ast
import  numpy as np
import pandas as pd
import os
import nibabel as nib
from scipy import io
from joblib import Memory
import abc
from abc import abstractmethod, ABCMeta
from imblearn.over_sampling import (RandomOverSampler, SMOTE, ADASYN, BorderlineSMOTE, SMOTENC)
from imblearn.under_sampling import (RandomUnderSampler,
                                    ClusterCentroids, 
                                    NearMiss,
                                    InstanceHardnessThreshold,
                                    CondensedNearestNeighbour,
                                    EditedNearestNeighbours,
                                    RepeatedEditedNearestNeighbours,
                                    AllKNN,
                                    NeighbourhoodCleaningRule,
                                    OneSidedSelection)
from imblearn.combine import SMOTEENN, SMOTETomek
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA, NMF
from sklearn.feature_selection import SelectPercentile, SelectKBest, SelectFromModel, f_classif,f_regression, RFE,RFECV, VarianceThreshold, mutual_info_classif, SelectFromModel
from sklearn.svm import LinearSVC, SVC, SVR
from sklearn.linear_model import LinearRegression, LogisticRegression, Lasso, LassoCV, RidgeCV, RidgeClassifier, BayesianRidge, ElasticNetCV
from sklearn.gaussian_process import  GaussianProcessClassifier, GaussianProcessRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, AdaBoostClassifier
from sklearn.model_selection import KFold, StratifiedKFold,  ShuffleSplit
from sklearn.pipeline import Pipeline


class BaseMachineLearning():
    """Base class for all machine learning

    Parameters:
    ----------
    configuration_file: file string
        configuration file containing all inputs

    Attributes:
    ----------
    method_feature_preprocessing_: list of sklearn object or None
    param_feature_preprocessing_: list of sklearn object or None
    
    method_dim_reduction_: list of sklearn object or None
    param_dim_reduction_: list of sklearn object or None
    
    method_feature_selection_: list of sklearn object or None
    param_feature_selection_: list of sklearn object or None
    
    method_unbalance_treatment_: list of sklearn object or None
    param_unbalance_treatment_: list of sklearn object or None
    
    machine_learning_type_: str
    method_machine_learning_: list of sklearn object or None
    param_machine_learning_: list of sklearn object or None

    method_model_ast.evaluation_: list of sklearn object or None
    param_model_evaluation_: list of sklearn object or None

    self.pipeline_: machine learning pipeline
    self.param_search_: parameter for search of machine learning pipeline
    """

    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        self.__random_state = 0

    def get_configuration_(self):
        """Get and parse the configuration file
        """

        with open(self.configuration_file, 'r', encoding='utf-8') as config:
                    configuration = config.read()
        self.configuration = json.loads(configuration)

        return self

    def get_preprocessing_parameters(self):
        self.method_feature_preprocessing_ = None
        self.param_feature_preprocessing_ = {}
                
        feature_preprocessing = self.configuration.get('feature_engineering', {}).get('feature_preprocessing', None)
        if feature_preprocessing and (list(feature_preprocessing.keys())[0] != 'None'):
            self.method_feature_preprocessing_ = [list(feature_preprocessing.keys())[0] if list(feature_preprocessing.keys())[0] != 'None' else None]
            self.method_feature_preprocessing_ = [self.security_eval(self.method_feature_preprocessing_[0])]
    
            for key in feature_preprocessing.keys():
                for key_ in feature_preprocessing.get(key).keys():
                    if key_ != []:
                        for key__ in feature_preprocessing.get(key).get(key_).keys():

                            param = feature_preprocessing.get(key).get(key_).get(key__)
                            param = 'None' if param == '' else param
                            # Parse parameters: if param is digits str or containing "(" and ")", we will eval the param
                            param = self.security_eval(param)
                            self.param_feature_preprocessing_.update({"feature_preprocessing__"+key_: [param]})

        # Fix the random_state for replication of results
        if "random_state" in self.method_feature_preprocessing_[0].get_params().keys():
            self.param_feature_preprocessing_.update({"feature_preprocessing__"+'random_state': [self.__random_state]})
        self.param_feature_preprocessing_ = None if self.param_feature_preprocessing_ == {} else self.param_feature_preprocessing_
             
        return self

    def get_dimension_reduction_parameters(self):
        self.method_dim_reduction_ = None
        self.param_dim_reduction_ = {}
                
        dimension_reduction = self.configuration.get('feature_engineering', {}).get('dimreduction', None)
        if dimension_reduction and (list(dimension_reduction.keys())[0] != 'None'):
            self.method_dim_reduction_ = [self.security_eval(list(dimension_reduction.keys())[0] if list(dimension_reduction.keys())[0] != 'None' else None)]
    
            for key in dimension_reduction.keys():
                for key_ in dimension_reduction.get(key).keys():
                    if key_ != []:
                        for key__ in dimension_reduction.get(key).get(key_).keys():
                            param = dimension_reduction.get(key).get(key_).get(key__)
                            param = 'None' if param == '' else param
                            # Parse parameters: if param is digits str or containing "(" and ")", we will eval the param
                            param = self.security_eval(param)
                            if not isinstance(param, (list, tuple)):
                                param = [param]
                            self.param_dim_reduction_.update({"dim_reduction__"+key_: param})
        
        # Fix the random_state for replication of results
        if "random_state" in self.method_dim_reduction_[0].get_params().keys():
            self.param_dim_reduction_.update({"dim_reduction__"+'random_state': [self.__random_state]})
        self.param_dim_reduction_ = None if self.param_dim_reduction_ == {} else self.param_dim_reduction_
        return self  

    def get_feature_selection_parameters(self):
        self.method_feature_selection_ = None
        self.param_feature_selection_ = {}
        
        feature_selection = self.configuration.get('feature_engineering', {}).get('feature_selection', None)
        if feature_selection and (list(feature_selection.keys())[0] != 'None'): 
            self.method_feature_selection_ = [self.security_eval(list(feature_selection.keys())[0])]
            for key in feature_selection.keys():
                for key_ in feature_selection.get(key).keys():
                    if key_ != []:
                        for key__ in feature_selection.get(key).get(key_).keys():
                            param = feature_selection.get(key).get(key_).get(key__)
                            param = 'None' if param == '' else param
                            # Parse parameters: if param is digits str or containing "(" and ")", we will eval the param
                            param = self.security_eval(param)
                            if not isinstance(param, (list, tuple)):
                                param = [param]
                            self.param_feature_selection_.update({"feature_selection__"+key_:param})

            # Methods
            self.method_feature_selection_ = list(feature_selection.keys())[0] if list(feature_selection.keys())[0] != 'None' else None
            # Update point
            if self.method_feature_selection_ == 'RFECV()':
                self.method_feature_selection_ = "RFECV(estimator=SVC(kernel='linear'))"
            
            if self.method_feature_selection_ == 'SelectFromModel(LassoCV())':
                self.method_feature_selection_ = 'SelectFromModel(LassoCV())'
                self.param_feature_selection_ = None
            
            if self.method_feature_selection_ == 'SelectFromModel(ElasticNetCV())':
                self.method_feature_selection_ = 'SelectFromModel(ElasticNetCV('
                for keys in list(self.param_feature_selection_.keys()):
                    param_ = keys.split('__')[1]
                    value_ = self.param_feature_selection_[keys]
                    self.method_feature_selection_ = self.method_feature_selection_+ f'{param_}={value_},'  
                self.method_feature_selection_ = self.method_feature_selection_ + '))'
                self.param_feature_selection_ = None
                
            self.method_feature_selection_ = [self.security_eval(self.method_feature_selection_)]
        
        # Fix the random_state for replication of results
        if "random_state" in self.method_feature_selection_[0].get_params().keys():
            self.param_feature_selection_.update({"feature_selection__"+'random_state': [self.__random_state]})
        self.param_feature_selection_ = None if self.param_feature_selection_ == {} else self.param_feature_selection_
        return self

    def get_unbalance_treatment_parameters(self):
        self.method_unbalance_treatment_ = None
        self.param_unbalance_treatment_ = {}

        unbalance_treatment = self.configuration.get('feature_engineering', {}).get('unbalance_treatment', None)
        if unbalance_treatment and (list(unbalance_treatment.keys())[0] != 'None'):
            self.method_unbalance_treatment_ = (self.security_eval(list(unbalance_treatment.keys())[0]) if list(unbalance_treatment.keys())[0] != 'None' else None)
    
            for key in unbalance_treatment.keys():
                for key_ in unbalance_treatment.get(key).keys():
                    if key_ != []:
                        for key__ in unbalance_treatment.get(key).get(key_).keys():

                            param = unbalance_treatment.get(key).get(key_).get(key__)
                            param = 'None' if param == '' else param
                            # Parse parameters: if param is digits str or containing "(" and ")", we will eval the param
                            param = self.security_eval(param)
                            if not isinstance(param, (list, tuple)):
                                param = [param]
                            self.param_unbalance_treatment_.update({"unbalance_treatment__"+key_:param})
                     
        # Fix the random_state for replication of results
        if "random_state" in self.method_unbalance_treatment_.get_params().keys():
            self.method_unbalance_treatment_.set_params(**{"random_state": self.__random_state})
            self.param_unbalance_treatment_.update({"unbalance_treatment__"+'random_state': [self.__random_state]})
        self.param_unbalance_treatment_ = None if self.param_unbalance_treatment_ == {} else self.param_unbalance_treatment_
        
        return self

    def get_machine_learning_parameters(self):
        self.method_machine_learning_ = None
        self.param_machine_learning_ = {}
        
        machine_learning = self.configuration.get('machine_learning', None)
        self.machine_learning_type_ = list(machine_learning.keys()) if machine_learning else None
        if self.machine_learning_type_ is None:
            raise ValueError("There is no keys for machine_learning")
        elif len(self.machine_learning_type_) > 1:
            raise RuntimeError("Currently, easylearn only supports one type of machine learning")
            
        for keys in machine_learning:
            machine_learning = machine_learning.get(keys, None)

        if machine_learning and (list(machine_learning.keys())[0] != 'None'):
            # TODO: This place will update for supporting multiple estimators
            self.method_machine_learning_ = [self.security_eval(list(machine_learning.keys())[0] if list(machine_learning.keys())[0] != 'None' else None)]
    
            for key in machine_learning.keys():
                for key_ in machine_learning.get(key).keys():
                    if key_ != []:
                        for key__ in machine_learning.get(key).get(key_).keys():

                            param = machine_learning.get(key).get(key_).get(key__)
                            param = 'None' if param == '' else param
                            # Parse parameters: if param is digits str or containing "(" and ")", we will eval the param
                            # for example, DecisionTreeClassifier(max_depth=1) is a parameter of AdaBoostClassifier()
                            # Because a [sklearn] object has a
                            param = self.security_eval(param)
                            if not isinstance(param, (list, tuple)):
                                param = [param]
                            # TODO: Design a method to set params
                            self.param_machine_learning_.update({"estimator__"+key_: param})
         
        # Fix the random_state for replication of results
        if "random_state" in self.method_machine_learning_[0].get_params().keys():
            self.param_machine_learning_.update({"estimator__"+'random_state': [self.__random_state]})
        self.param_machine_learning_ = None if self.param_machine_learning_ == {} else self.param_machine_learning_
        return self

    def get_model_evaluation_parameters(self):
        self.method_model_evaluation_ = None
        self.param_model_evaluation_ = {}
        self.Statistical_analysis = self.configuration.get('model_evaluation', {}).get("Statistical_analysis", None)
        if self.Statistical_analysis:
            self.configuration.get('model_evaluation', {}).pop("Statistical_analysis")
        model_evaluation = self.configuration.get('model_evaluation', None)
        
        if model_evaluation and (list(model_evaluation.keys())[0] != 'None'):
            self.method_model_evaluation_ = list(model_evaluation.keys())[0] if list(model_evaluation.keys())[0] != 'None' else None
            
            for key in model_evaluation.keys():
                for key_ in model_evaluation.get(key).keys():
                    if key_ != []:
                        for key__ in model_evaluation.get(key).get(key_).keys():                            
                            param = model_evaluation.get(key).get(key_).get(key__)
                            param = 'None' if param == '' else param
                            # Parse parameters: if param is digits str or containing "(" and ")", we will eval the param
                            # for example, DecisionTreeClassifier(max_depth=1) is a parameter of AdaBoostClassifier()
                            # Because a [sklearn] object has a
                            if type(param) is str:  # selected_dataset is list
                                    param = self.security_eval(param)
                            self.param_model_evaluation_.update({key_: param})
             
            # ------Give parameter to method------
            pme = ""
            ik_end = len(self.param_model_evaluation_)  - 1
            for ik, key_pme in enumerate(self.param_model_evaluation_):
                if ik != ik_end:
                    pme = pme + f"{key_pme}={self.param_model_evaluation_[key_pme]}" + ", "
                else:
                    pme = pme + f"{key_pme}={self.param_model_evaluation_[key_pme]}"
            
            self.method_model_evaluation_ = self.method_model_evaluation_.split("(")[0] + "(" + pme + self.method_model_evaluation_.split("(")[1]
            self.method_model_evaluation_ = self.security_eval(self.method_model_evaluation_)
            
        return self

    def get_statistical_analysis_parameters(self):
        self.Statistical_analysis = self.configuration.get('model_evaluation', {}).get("Statistical_analysis", None)
        return self

    def get_visualization_parameters(self):
        self.configuration.get('visualization', None)

    def get_all_inputs(self):
        self.get_configuration_()
        self.get_preprocessing_parameters()
        self.get_dimension_reduction_parameters()
        self.get_feature_selection_parameters()
        self.get_unbalance_treatment_parameters()
        self.get_machine_learning_parameters()
        self.get_model_evaluation_parameters()
        return self


    @staticmethod
    def security_eval(expression):
        """Security evaluation of python expression
        
        FIX: 'eval' had security hole
        """
        
        iseval = (
                    (
                        bool(re.search(r'\d', expression)) or 
                        (expression == 'None') or 
                        (bool(re.search(r'\(', expression)) and bool(re.search(r'\)', expression))) 
                    ) 
                    and
                    (
                        expression != 'l1' and
                        expression != 'l2'
                        # not bool(re.search('del',  expression)) and
                        # not bool(re.search('open',  expression)) and
                        # not bool(re.search('move',  expression)) and
                        # not bool(re.search('copy',  expression))     
                    )
        )

        if iseval:
            evaluated_expression = eval(expression)
        else:
            evaluated_expression = expression

        return evaluated_expression

    def make_pipeline_(self):
        
        """Construct pipeline_

        Currently, the pipeline_ only supports one specific method for corresponding method, 
        e.g., only supports one dimension reduction method for dimension reduction.
        In the next version, the pipeline_ will support multiple methods for each corresponding method.
        """
        
        self.memory = Memory(location=os.path.dirname(self.configuration_file), verbose=False)

        self.pipeline_ = Pipeline(steps=[
            ('feature_preprocessing','passthrough'),
            ('dim_reduction', 'passthrough'),
            ('feature_selection', 'passthrough'),
            ('estimator', 'passthrough'),
            ], 
            memory=self.memory
        )

        # Set parameters of gridCV
        self.param_search_ = {}

        if self.method_feature_preprocessing_:
            self.param_search_.update({'feature_preprocessing':self.method_feature_preprocessing_})
        if self.param_feature_preprocessing_:   
            self.param_search_.update(self.param_feature_preprocessing_)
            
        if self.method_dim_reduction_:
            self.param_search_.update({'dim_reduction':self.method_dim_reduction_})
        if self.param_dim_reduction_:
            self.param_search_.update(self.param_dim_reduction_)
                
        if self.method_feature_selection_:
            self.param_search_.update({'feature_selection': self.method_feature_selection_})
        if self.param_feature_selection_:
            self.param_search_.update(self.param_feature_selection_)
            
        if self.method_machine_learning_:
            self.param_search_.update({'estimator': self.method_machine_learning_})
        if self.param_machine_learning_:
            self.param_search_.update(self.param_machine_learning_)
        
        self.is_search = self.get_is_search(self.param_search_)
        if not self.is_search:
            
            if self.method_feature_preprocessing_:
                self.pipeline_.set_params(**{'feature_preprocessing':self.method_feature_preprocessing_[0]})
            if self.param_feature_preprocessing_:   
                self.pipeline_['feature_preprocessing'].set_params(self.param_feature_preprocessing_)
                
            if self.method_dim_reduction_:
                self.pipeline_.set_params(**{'dim_reduction':self.method_dim_reduction_[0]})
            if self.param_dim_reduction_:
                mapping = self.parse_search_params(self.param_dim_reduction_)
                self.pipeline_['dim_reduction'].set_params(**mapping)   
                
            if self.method_feature_selection_:
                self.pipeline_.set_params(**{'feature_selection': self.method_feature_selection_[0]})
            if self.param_feature_selection_:
                mapping = self.parse_search_params(self.param_feature_selection_)
                self.pipeline_['feature_selection'].set_params(**mapping)

            if self.method_machine_learning_:
                self.pipeline_.set_params(**{'estimator': self.method_machine_learning_[0]})
            if self.param_machine_learning_:
                mapping = self.parse_search_params(self.param_machine_learning_)
                self.pipeline_['estimator'].set_params(**mapping)

        return self
    
    @staticmethod
    def get_is_search(dictionary):
        """ Identify whether search params or just using pipeline
        """
        
        is_search = False
        for key in dictionary:
            if dictionary[key] and len(dictionary[key]) > 1:
                is_search = True
                break
    
        return is_search
    
    @staticmethod
    def parse_search_params(dictionary):
        mapping = {}
        for key in dictionary:
            mapping.update({key.split("__")[1]:dictionary[key][0]})
        return mapping
            
      
class DataLoader(BaseMachineLearning):
    """Load datasets according to different data types
    
    Parameters:
    ----------
    configuration_file: file string
        configuration file containing all inputs

    Attributes:
    ----------
    targets_: ndarray of shape (n_samples, )
    
    features_: ndarray of shape (n_samples, n_features) 

    mask_: dictionary, each element contains a mask of a modality of a group
    """
    
    def __init__(self, configuration_file):
        super(DataLoader, self).__init__(configuration_file)
        
        # Generate type2fun dictionary
        # TODO: Extended to handle other formats
        self.type2fun = {".nii": self.read_nii, 
                    ".mat": self.read_mat, 
                    ".txt": self.read_txt,
                    ".xlsx": self.read_excel,
                    ".xls": self.read_excel,
        }

    def load_data(self):
        self.get_configuration_()
        self.data_loading = self.configuration.get('data_loading', None)
        
        # ======Check datasets======
        # NOTE.: That check whether the feature dimensions of the same modalities in different groups are equal
        # is placed in the next section.
        targets = {}
        self.covariates_ = {}
        for i, gk in enumerate(self.data_loading.keys()):
            
            # Check the number of modality across all group is equal
            if i == 0:
                n_mod = len(self.data_loading.get(gk).get("modalities").keys())
            else:
                if n_mod != len(self.data_loading.get(gk).get("modalities").keys()):
                    raise ValueError("The number of modalities in each group is not equal, check your inputs")
                    return
                n_mod = len(self.data_loading.get(gk).get("modalities").keys())
                
            # Get targets
            targets_input = self.data_loading.get(gk).get("targets")
            targets[gk] = self.read_targets(targets_input)            
    
            # Get covariates
            covariates_input = self.data_loading.get(gk).get("covariates")
            self.covariates_[gk] = self.base_read(covariates_input)
            
            # Check the number of files in each modalities in the same group is equal
            for j, mk in enumerate(self.data_loading.get(gk).get("modalities").keys()):
                modality = self.data_loading.get(gk).get("modalities").get(mk)
                
                # Filses
                file_input = modality.get("file")
                if j == 0:
                    n_file = self.get_file_len(file_input)  # Initialize n_file
                else:
                    if n_file != self.get_file_len(file_input):  # Left is previous, right is current loop
                        raise ValueError(f"The number of files in each modalities in {gk} is not equal, check your inputs")
                        return
                n_file = self.get_file_len(file_input)  # Update n_file

                # Check the number of targets in each modalities is equal to the number of files          
                # If the type of targets is list, and number of files are not equal to targets, then raise error
                if (isinstance(targets[gk],list)) and (n_file != len(targets[gk])):
                    raise ValueError(f"The number of files in {mk} of {gk} is not equal to the number of targets, check your inputs")
                    return
        
                # Check the number of lines of covariates in each modalities is equal to the number of files
                # If covariates is not int (0), and number of files are not equal to covariates, then raise error
                if (not isinstance(self.covariates_[gk],int)) and (n_file != len(self.covariates_[gk])):
                    raise ValueError(f"The number of files in {mk} of {gk} is not equal to its' number of covariates, check your inputs")
                    return
                
        # ======Get selected datasets======
        shape_of_data = {}
        feature_applied_mask_and_add_otherinfo = {}
        col_drop = {}
        self.mask_ = {}
        for ig, gk in enumerate(self.data_loading.keys()):            
            shape_of_data[gk] = {}
            feature_applied_mask_and_add_otherinfo[gk] = {}
            self.mask_[gk] = {}
            
            for jm, mk in enumerate(self.data_loading.get(gk).get("modalities").keys()):
                modality = self.data_loading.get(gk).get("modalities").get(mk)
               
                # Get file
                file_input = modality.get("file")
                n_file = self.get_file_len(file_input)
                if len(file_input) == 1:
                    one_file_per_modality = True
                else:
                    one_file_per_modality = False
                
                # Get cases' name in this modality
                # The file name must contain r'.*(sub.?[0-9].*).*'
                # TODD: BIDS format
                subj_name = self.extract_id(file_input, n_file)
                
                # Sort targets and check
                if (isinstance(targets[gk],int)):
                    targets[gk] = [targets[gk] for ifile in range(n_file)]
                    targets[gk] = pd.DataFrame(targets[gk])
                    targets[gk]["ID"] = subj_name["ID"]
                    targets[gk].rename(columns={0: "__targets__"}, inplace=True)
                else:
                    if not isinstance(targets[gk], pd.core.frame.DataFrame):
                        targets[gk] = pd.DataFrame(targets[gk])                    
                    if one_file_per_modality:
                        self.targets[gk]["ID"] = subj_name["ID"]
                    elif (not one_file_per_modality) and ("ID" not in targets[gk].columns):
                        raise ValueError(f"The targets of {gk} did not have 'ID' column, check your targets")
                        return                      
                targets[gk] = pd.merge(subj_name, targets[gk], left_on="ID", right_on="ID", how='inner')
                if targets[gk].shape[0] != n_file:
                        raise ValueError(f"The subjects' ID in targets is not totally matched with its' data file name in {mk} of {gk} , check your ID in targets or check your data file name")
                        return

                # Sort covariates and check                
                if (not isinstance(self.covariates_[gk],int)): 
                    if one_file_per_modality:
                        self.covariates_[gk]["ID"] = subj_name["ID"]
                    if ("ID" not in self.covariates_[gk].columns):
                        raise ValueError(f"The covariates of {gk} did not have 'ID' column, check your covariates")
                        return 
                    else:
                        self.covariates_[gk] = pd.merge(subj_name, self.covariates_[gk], left_on="ID", right_on="ID") 
                        if self.covariates_[gk].shape[0] != n_file:
                            raise ValueError(f"The subjects' ID in covariates is not totally matched with its' data file name in {mk} of {gk} , check your ID in covariates or check your data file name")
                            return 
                        if jm == 0:
                            # Get columns for drop (Remain 'ID' for matching)
                            columns_of_covariates = list(set(self.covariates_[gk].columns) - set(["ID"]))
                            [self.covariates_[gk].rename(columns={colname: f"__{colname}__"}, inplace=True) for colname in columns_of_covariates]
                            col_drop[gk] = list((set(self.covariates_[gk].columns) | set(targets[gk].columns)) ^ set(["ID"]))
                           
                # Get Features
                # If only input one file for one modality in a given group, then I think the file contained multiple cases' data
                feature_all = self.read_file(file_input, False)
                
                # Mask
                mask_input = modality.get("mask")
                self.mask_[gk][mk] = self.base_read(mask_input)
                if not isinstance(self.mask_[gk][mk], int):  # If mask is empty then give 0 to mask
                   self.mask_[gk][mk] = self.mask_[gk][mk] != 0
                   # Apply mask
                   feature_applied_mask = [fa[self.mask_[gk][mk]] for fa in feature_all]
                   feature_applied_mask = np.array(feature_applied_mask)
                else:
                   feature_applied_mask = [fa for fa in feature_all]
                   feature_applied_mask = np.array(feature_applied_mask)
                   feature_applied_mask = feature_applied_mask.reshape(n_file,-1)
                   
                # Add subj_name, targets and covariates to features for matching datasets across modalities in the same group 
                if (not isinstance(self.covariates_[gk],int)): 
                    feature_applied_mask_and_add_otherinfo[gk][mk] = pd.concat([subj_name, targets[gk]["__targets__"], self.covariates_[gk].drop(["ID"], axis=1,inplace=False), pd.DataFrame(feature_applied_mask)], axis=1)  
                else:
                    feature_applied_mask_and_add_otherinfo[gk][mk] = pd.concat([subj_name, targets[gk]["__targets__"], pd.DataFrame(feature_applied_mask)], axis=1)  
                
                # Check whether the feature dimensions of the same modalities in different groups are equal
                shape_of_data[gk][mk] = feature_applied_mask.shape
                if ig == 0:
                   gk_pre = gk
                else:
                    if shape_of_data[gk_pre][mk][-1] != shape_of_data[gk][mk][-1]:
                        raise ValueError(f"Feature dimension of {mk} in {gk_pre} is {shape_of_data[gk_pre][mk][-1]} which is not equal to {mk} in {gk}: {shape_of_data[gk][mk][-1]}, check your inputs")
                        return                
            
            # Update gk_pre for check feature dimension
            gk_pre = gk            
                
        # Concatenate all modalities and targets
        # Modalities of one group must have the same ID so that to mach them.
        for gi, gk in enumerate(feature_applied_mask_and_add_otherinfo):
            for mi, mk in enumerate(feature_applied_mask_and_add_otherinfo[gk]):
                # Concat feature across different modalities in the same group
                # Sort with the first modality
                if mi == 0:
                    feature_sorted = feature_applied_mask_and_add_otherinfo[gk][mk]
                if mi != 0:
                    feature_for_concat = feature_applied_mask_and_add_otherinfo[gk][mk].drop(col_drop[gk], axis=1)
                    feature_sorted = pd.merge(feature_sorted, feature_for_concat, left_on="ID", right_on="ID", how="left")
                    feature_sorted.drop(self.covariates_[gk].columns, axis=1, inplace=True)
            
            # Concat feature across different group
            if gi == 0:
                self.features_ = feature_sorted 
            else:
                self.features_ = pd.concat([self.features_, feature_sorted], axis=0)
            
        self.targets_ = self.features_["__targets__"].values
        self.features_.drop(["__targets__", "ID"], axis=1, inplace=True)
        self.features_ =  self.features_.values
        return self
       
    #%% -----------------------------utilts------------------------------------
    def get_file_len(self, files):
        """If the files lenght is 1, then the length is the lenght of content of the files
        """
        
        file_len = len(files)
        if file_len == 1:
            feature_all = self.read_file(files, False)
            feature_all = [fe for fe in feature_all][0]
            file_len = len(feature_all)
        return file_len
    
    def read_file(self, file_input, to1d=False):  
        data = (self.base_read(file, to1d) for file in file_input)
        return data

    def read_targets(self, targets_input):
        if (targets_input == []) or (targets_input == ''):
            return None
        
        elif os.path.isfile(targets_input):
            return self.base_read(targets_input) 
        
        elif len(re.findall(r'[A-Za-z]', targets_input)):  # Contain alphabet
            raise ValueError(f"The targets(labels) must be an Arabic numbers or file, but it contain alphabet, check your targets: '{targets_input}'")
            return
        
        elif ' ' in targets_input:
            targets = targets_input.split(' ')
            return [int(targets_) for targets_ in targets]
        
        elif ',' in targets_input:
            targets = targets_input.split(',')
            return [int(targets_) for targets_ in targets]
             
        else:
            return eval(targets_input)

    def base_read(self, file, to1d=False):
        """Read data for one case
        
        Parameters:
        ----------
        file: Path str
            input file of one case
        
        to1d: Bool
            whether transform data to 1 dimension
        
        Return:
        ------
        data: ndarray
        """
        
        if (file == []) or (file == ''):
            return 0
        elif not os.path.isfile(file):
            raise ValueError(f" Cannot find the file:'{file}'")
            return
        else:
            # Identify file type
            [path, filename] = os.path.split(file)
            suffix = os.path.splitext(filename)[-1]
            # Read
            data = self.type2fun[suffix](file)
            
            if to1d:
                data = np.reshape(data, [-1,])
                
        return data
    
    @ staticmethod
    def read_nii(file):      
        obj = nib.load(file)
        data = obj.get_fdata()
        return data

    @ staticmethod
    def read_mat(file):
        dataset_struct = io.loadmat(file)
        data = dataset_struct[list(dataset_struct.keys())[3]]
        
        # If data is symmetric matrix, then only extract triangule matrix
        if len(data.shape) == 2:
            if data.shape[0] == data.shape[1]:                
                data_ = data.copy()
                data_[np.eye(data.shape[0]) == 1] = 0
                if np.all(np.abs(data_-data_.T) < 1e-8):
                    return data[np.triu(np.ones(data.shape),1)==1]
        
        return data

    @ staticmethod
    def read_txt(file):
        data = pd.read_csv(file)
        
        # If data is symmetric matrix, then only extract triangule matrix
        if (len(data.shape) == 2) and (data.shape[0] == data.shape[1]):                
                data_ = data.copy()
                data_[np.eye(data.shape[0]) == 1] = 0
                if np.all(np.abs(data_-data_.T) < 1e-8):
                    return data[np.triu(np.ones(data.shape),1)==1]
                                    
        return data

    @ staticmethod
    def read_excel(file):
        """
        Not consider symmetric matrix
        """
        
        data = pd.read_excel(file)
        return data
    
    @staticmethod
    def extract_id(files, n_file):
        """Extract subject unique ID from file names
        """
        
        file_len = len(files)
        if file_len > 1:
            subj_name = [os.path.basename(file).split(".")[0] for file in files]
            subj_name = [re.findall(r'.*(sub.?[0-9].*).*', name)[0] if re.findall(r'.*(sub.?[0-9].*).*', name) != [] else "" for name in subj_name]
        else:
            subj_name = [f"sub-{i}" for i in range(n_file)]
        subj_name = pd.DataFrame(subj_name)
        subj_name.columns = ["ID"]
        return subj_name


if __name__ == '__main__':
    base = BaseMachineLearning(configuration_file=r'D:\My_Codes\virtualenv_eslearn\Lib\site-packages\eslearn\GUI\test\configuration_file.json')
    data_loader = DataLoader(configuration_file=r'D:\My_Codes\virtualenv_eslearn\Lib\site-packages\eslearn\GUI\test\configuration_file.json')
    data_loader.load_data()
    
    base.get_configuration_()
    base.get_preprocessing_parameters()
    base.get_dimension_reduction_parameters()
    base.get_feature_selection_parameters()
    base.get_unbalance_treatment_parameters()
    base.get_machine_learning_parameters()
    base.get_model_evaluation_parameters()
    

    print(base.method_feature_preprocessing_)
    print(base.param_feature_preprocessing_)
    
    print(base.method_dim_reduction_)
    print(base.param_dim_reduction_)
    
    print(base.method_feature_selection_)
    print(base.param_feature_selection_)
    
    print(base.method_unbalance_treatment_)
    print(base.param_unbalance_treatment_)
    
    print(base.method_machine_learning_)
    print(base.param_machine_learning_)

    print(base.method_model_evaluation_)
    print(base.param_model_evaluation_)

    