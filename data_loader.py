# load the .mat file
import scipy.io as sio
import scipy.sparse
import numpy as np

class Trial:
    def __init__(self, trialNum, startDateNum, startDateStr, timeTargetOn, timeTargetAcquire, timeTargetHeld, timeTrialEnd, subject, counter, state, cursorPos, spikeRaster, spikeRaster2, isSuccessful, timeFirstTargetAcquire, timeLastTargetAcquire, trialLength, target):
        self.fields = ['trialNum', 'startDateNum', 'startDateStr', 'timeTargetOn', 'timeTargetAcquire', 'timeTargetHeld', 'timeTrialEnd', 'subject', 'counter', 'state', 'cursorPos', 'spikeRaster', 'spikeRaster2', 'isSuccessful', 'timeFirstTargetAcquire', 'timeLastTargetAcquire', 'trialLength', 'target']
        self.trialNum = trialNum
        self.startDateNum = startDateNum
        self.startDateStr = startDateStr
        self.timeTargetOn = timeTargetOn
        self.timeTargetAcquire = timeTargetAcquire
        self.timeTargetHeld = timeTargetHeld
        self.timeTrialEnd = timeTrialEnd
        self.subject = subject
        self.counter = counter
        self.state = state
        self.cursorPos = cursorPos
        self.spikeRaster = spikeRaster
        self.spikeRaster2 = spikeRaster2
        self.isSuccessful = isSuccessful
        self.timeFirstTargetAcquire = timeFirstTargetAcquire
        self.timeLastTargetAcquire = timeLastTargetAcquire
        self.trialLength = trialLength
        self.target = target

    def __str__(self):
        return 'trialNum: ' + str(self.trialNum) + '\nstartDateNum: ' + str(self.startDateNum) + '\nstartDateStr: ' + str(self.startDateStr) + '\ntimeTargetOn: ' + str(self.timeTargetOn) + '\ntimeTargetAcquire: ' + str(self.timeTargetAcquire) + '\ntimeTargetHeld: ' + str(self.timeTargetHeld) + '\ntimeTrialEnd: ' + str(self.timeTrialEnd) + '\nsubject: ' + str(self.subject) + '\ncounter: ' + str(self.counter) + '...\nstate: ' + str(self.state) + '\ncursorPos: ' + str(self.cursorPos) + '\nspikeRaster: ' + str(self.spikeRaster) + '\nspikeRaster2: ' + str(self.spikeRaster2) + '\nisSuccessful: ' + str(self.isSuccessful) + '\ntimeFirstTargetAcquire: ' + str(self.timeFirstTargetAcquire) + '\ntimeLastTargetAcquire: ' + str(self.timeLastTargetAcquire) + '\ntrialLength: ' + str(self.trialLength) + '\ntarg: ' + str(self.target)
    
    def __repr__(self):
        return 'trialNum: ' + self.trialNum.__repr__() + '\nstartDateNum: ' + self.startDateNum.__repr__() + '\nstartDateStr: ' + self.startDateStr.__repr__() + '\ntimeTargetOn: ' + self.timeTargetOn.__repr__() + '\ntimeTargetAcquire: ' + self.timeTargetAcquire.__repr__() + '\ntimeTargetHeld: ' + self.timeTargetHeld.__repr__() + '\ntimeTrialEnd: ' + self.timeTrialEnd.__repr__() + '\nsubject: ' + self.subject.__repr__() + '\ncounter: np.ndarray with shape ' + str(self.counter.shape) + ' ' + self.counter.dtype.name + '\nstate: np.ndarray with shape ' + str(self.state.shape) + ' ' + self.state.dtype.name + '\ncursorPos: np.ndarray with shape ' + str(self.cursorPos.shape) + ' ' + self.cursorPos.dtype.name + '\nspikeRaster: ' + self.spikeRaster.__repr__() + '\nspikeRaster2: ' + self.spikeRaster2.__repr__() + '\nisSuccessful: ' + self.isSuccessful.__repr__() + '\ntimeFirstTargetAcquire: ' + self.timeFirstTargetAcquire.__repr__() + '\ntimeLastTargetAcquire: ' + self.timeLastTargetAcquire.__repr__() + '\ntrialLength: ' + self.trialLength.__repr__() + '\ntarget: ' + self.target.__repr__()

class JRDataset:
    def __init__(self, matlab_file_path='JR_2015-12-04_truncated2.mat', **kwargs):
        if (matlab_file_path == None and 'matlab' in kwargs):
            matlab_file_path = kwargs['matlab']
        elif (matlab_file_path == None):
            self.fields = ['startDateNum', 'startDateStr', 'timeTargetOn', 'timeTargetAcquire', 'timeTargetHeld', 'timeTrialEnd', 'subject', 'counter', 'state', 'cursorPos', 'spikeRaster', 'spikeRaster2', 'isSuccessful', 'trialNum', 'timeFirstTargetAcquire', 'timeLastTargetAcquire', 'trialLength', 'target']
            # assert that kwargs belongs to the list of fields
            for key in kwargs:
                assert key in self.fields, 'Field not found: ' + key
            # set the fields to the kwargs
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
        # try to load the file but if you cant the print an error
            try:
                self.matlab = sio.loadmat(matlab_file_path)
            except FileNotFoundError:
                print('Could not find file: ' + matlab_file_path)
            data = self.matlab
            self.fields = list(data['R'].dtype.names)
            self.startDateNum = np.array([data['R'][self.fields[0]][0][i][0][0] for i in range(len(data['R'][self.fields[0]][0]))])
            self.startDateStr = np.array([data['R'][self.fields[1]][0][i][0] for i in range(len(data['R'][self.fields[1]][0]))])
            self.timeTargetOn = np.array([data['R'][self.fields[2]][0][i][0][0] for i in range(len(data['R'][self.fields[2]][0]))])
            self.timeTargetAcquire = np.array([data['R'][self.fields[3]][0][i][0][0] for i in range(len(data['R'][self.fields[3]][0]))])
            self.timeTargetHeld = np.array([data['R'][self.fields[4]][0][i][0][0] for i in range(len(data['R'][self.fields[4]][0]))])
            self.timeTrialEnd = np.array([data['R'][self.fields[5]][0][i][0][0] for i in range(len(data['R'][self.fields[5]][0]))])
            self.subject = np.array([data['R'][self.fields[6]][0][i][0] for i in range(len(data['R'][self.fields[6]][0]))])
            self.counter = ([np.array(data['R'][self.fields[7]][0][i][0].reshape(1, len(data['R'][self.fields[7]][0][i][0])), dtype=np.float32) for i in range(len(data['R'][self.fields[7]][0]))])
            self.state = ([np.array(data['R'][self.fields[8]][0][i][0].reshape(1, len(data['R'][self.fields[8]][0][i][0])), dtype=np.float32) for i in range(len(data['R'][self.fields[8]][0]))])
            self.cursorPos = ([np.array(data['R'][self.fields[9]][0][i], dtype=np.float32) for i in range(len(data['R'][self.fields[9]][0]))])
            self.spikeRaster = ([(data['R'][self.fields[10]][0][i]) for i in range(len(data['R'][self.fields[10]][0]))])
            self.spikeRaster2 = ([(data['R'][self.fields[11]][0][i]) for i in range(len(data['R'][self.fields[11]][0]))])
            self.isSuccessful = np.array([data['R'][self.fields[12]][0][i][0][0] for i in range(len(data['R'][self.fields[12]][0]))])
            self.trialNum = np.array([data['R'][self.fields[13]][0][i][0][0] for i in range(len(data['R'][self.fields[13]][0]))])
            self.timeFirstTargetAcquire = np.array([data['R'][self.fields[14]][0][i][0][0] for i in range(len(data['R'][self.fields[14]][0]))])
            self.timeLastTargetAcquire = np.array([data['R'][self.fields[15]][0][i][0][0] for i in range(len(data['R'][self.fields[15]][0]))])
            self.trialLength = np.array([data['R'][self.fields[16]][0][i][0][0] for i in range(len(data['R'][self.fields[16]][0]))])
            self.target = np.array([(np.array([data['R'][self.fields[17]][0][i]]).reshape(3)) for i in range(len(data['R'][self.fields[17]][0]))])

        self.trials = []
        for i in range(len(self.trialNum)):
            self.trials.append(Trial(self.trialNum[i], self.startDateNum[i], self.startDateStr[i], self.timeTargetOn[i], self.timeTargetAcquire[i], self.timeTargetHeld[i], self.timeTrialEnd[i], self.subject[i], self.counter[i], self.state[i], self.cursorPos[i], self.spikeRaster[i], self.spikeRaster2[i], self.isSuccessful[i], self.timeFirstTargetAcquire[i], self.timeLastTargetAcquire[i], self.trialLength[i], self.target[i]))

        # stacked_spikes = scipy.sparse.hstack(tuple([train_data.spikeRaster[i] for i in range(len(train_data))]))
        self.stackedSpikeRaster = scipy.sparse.hstack(tuple([self.trials[i].spikeRaster for i in range(len(self.trials))]))
        self.stackedSpikeRaster2 = scipy.sparse.hstack(tuple([self.trials[i].spikeRaster2 for i in range(len(self.trials))]))
        self.stackedCursorPos = np.hstack(tuple([self.trials[i].cursorPos for i in range(len(self.trials))]))
        self.stackedState = np.hstack(tuple([self.trials[i].state for i in range(len(self.trials))]))

    def __iter__(self):
        return iter(self.trials)
    
    def __next__(self):
        return next(self.trials)
    
    def __getitem__(self, key):
        # we want to be able to index the dataset by trial number or slice it
        if isinstance(key, int):
            return self.trials[key]
        elif isinstance(key, slice):
            # return self.trials[key.start:key.stop:key.step]
            # we want to return a new dataset with the trials sliced
            kwargs = {}
            for field in self.fields:
                kwargs[field] = self.__getitem__(field)[key.start:key.stop:key.step]
            return JRDataset(matlab_file_path=None, **kwargs)
        # if it is a string, we want to check if it is a field name
        elif isinstance(key, str):
            if key in self.fields:
                return getattr(self, key)
            else:
                raise KeyError('Field not found: ' + key)
        else:
            raise KeyError('Key not found: ' + key)
        
    def __len__(self):
        return len(self.trials)
    