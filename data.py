from typing import Mapping, Iterator

import pickle
import torch
import torchvision
import torchvision.transforms as transforms
from problog.logic import Term, Constant

from deepproblog.dataset import Dataset
from deepproblog.query import Query

#labels have been modified
def CreateDataset(input = '/home/blackbeard/Documents/Τεχνητή Νοημοσύνη/3. Διπλωματική εργασία/MSc Project 2/NeurASP/data/3-fold_dict.pkl'):
    # Load the data
    with open('/home/blackbeard/Documents/Τεχνητή Νοημοσύνη/3. Διπλωματική εργασία/MSc Project 2/NeurASP/data/3-fold_dict.pkl', 'rb') as handle:
        data_dict = pickle.load(handle)

    fold_dict={
        "fold1":data_dict["fold1"],
        "fold2":data_dict["fold2"],
        "fold3":data_dict["fold3"]
    }

    # Split the data into train and test
    data = {'train': {}, 'test': {}}

    complex_train = []
    for f in fold_dict:
        for s in fold_dict[f]["train"]:
            if(len(s["models"])>0):
                complex_train.append((s['p1_tensor'].squeeze(0), s['complex_labels_as_list'][0]))


    complex_test = []
    for f in fold_dict:
        for s in fold_dict[f]["test"]:
            if(len(s["models"])>0):
                complex_test.append((s['p1_tensor'].squeeze(0), s['complex_labels_as_list'][0]))


    data['train'] = complex_train
    data['test'] = complex_test
    return data



transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

'''datasets = {
    "train": torchvision.datasets.MNIST(
        root='data/', train=True, download=True, transform=transform
    ),
    "test": torchvision.datasets.MNIST(
        root='data/', train=False, download=True, transform=transform
    ),
}'''

datasets = CreateDataset()

class CaviarFrames(Mapping[Term, torch.Tensor]):

    def __iter__(self) -> Iterator:
        for i in range(self.dataset):
            yield self.dataset[i][0]

    def __len__(self) -> int:
        return len(self.dataset)

    def __init__(self, subset):
        self.subset = subset
        self.dataset = datasets[self.subset]

    def __getitem__(self, item):
        return self.dataset[int(item[0])][0]


class CaviarDataset(Dataset):

    def __init__(self, subset):
        self.subset = subset
        self.dataset = datasets[subset]

    def __len__(self):
        return len(self.dataset) // 2

    def to_query(self, i: int) -> Query:
        #image1 = Term("tensor", Term(self.subset, Constant(i * 2)))
        #image2 = Term("tensor", Term(self.subset, Constant(i * 2 + 1)))
        #label = Constant(int(self.dataset[i*2][1] + self.dataset[i*2+1][1]))
        image1 = Term("tensor", Term(self.subset, Constant(0)))
        image2 = Term("tensor", Term(self.subset, Constant(0)))
        label = Constant(int(self.dataset[0][1] + self.dataset[0][1]))
        
        term = Term('addition', image1, image2, label)
        return Query(term)
