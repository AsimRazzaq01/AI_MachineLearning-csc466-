import numpy as np

class NaiveBaseClassification:
    def __init__(self, model_type="gaussuan"):
        self.model_type = model_type 
        self.classes = None 
        self.priors = None
        self.conditional_probs = None
        
    
    def fit(self,X,y):
        self.classes , class_count = np.unique(y,return_counts = True)
        self.priors = { c: count / len(y) for c,count in zip(self.classes, class_count) }
        self.conditional_probs = {}
        
        if self.model_type == "multinomial" :
            total_features = X.shape[1]
            self.conditional_probs = {c: {} for c in self.classes}
        
        