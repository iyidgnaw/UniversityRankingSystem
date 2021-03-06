# University Ranking System

Yearly rank of Research Institution and University has become a tradition for many popular newspapers, magazines and academic publications. The impact on global advancements is an essential standard of measurement on research institutes. It forms an interesting graph in ways that outstanding scientists tend to work in influential affiliations and leading companies tend to cooperate with authoritative institutes. The topic of KDD Cup 2016 is to find influential nodes in research community. The competition convert this problem into predicting the rank of paper acceptance number by several important conferences in research field. In this paper, we show ways of improving the Ensemble Model brought by Qian and Dong[7], who was ranked overall at 2nd place in KDD Cup 2016. We improved the overall accuracy of the ensemble model and discuss ways it might be further improved in future works. All extracted feature data and source code of our model implementations are publicly available in this repository for further research purposes.

Full Paper: [here](https://github.com/xueguangl23/UniversityRankingSystem/blob/master/Predicting%20Institution%20Ranking-%20Whose%20paper%20are%20accepted%20the%20most.pdf)

The Ranking SVM algorithm, SVM/svm_rank, written by [Thorsten Joachims](http://www.joachims.org/), is publically available for research purposes. For more information regarding this implementation of Ranking SVM, please refer to author's website [SVM_Rank](https://www.cs.cornell.edu/people/tj/svm_light/index.html). 

The SVM/svmparser.py can be used as a wrapper to call Joachims' Ranking SVM gcc excutables and get model and classify. 
