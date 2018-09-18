import pandas as pd

# class Prolog(object):
#     def __init__(self):
#         self.key = "PROLOG"
#         self.File_Format = None
#         self.Software = None
#         self.Data_prepared_by = None
#         self.Location = None
#         self.Date_Locale = None
#         self.Date = None

# class ChronostratigraphyScheme(object):
#     def __init__(self):
#         self.key = "Chronostratigraphy Scheme"
#         self.Scheme_name = None
#         self.Scheme_ID = None
#         self.Number_of_units = None

# class BiozonesScheme(object):
#     def __init__(self):
#         self.key = "Biozones Scheme"
#         self.cheme_name = None
#         self.Scheme_ID = None
#         self.Discipline = None
#         self.Number_of_units = None

# class LithostratigraphyScheme(object):
#     def __init__(self):
#         self.key = "Lithostratigraphy Scheme"
#         self.Scheme_name = None
#         self.Scheme_ID = None
#         self.Number_of_units = None

# class BiostratigraphicComment(object):
#     def __init__(self):
#         self.key = "BIOSTRATIGRAPHIC"
#         self.depth = None
#         self.sample_id = None
#         self.Discipline = None
#         self.Sample_ID = None
#         self.Analyst = None
#         self.Comment = None

class Sample(object):
    def __init__(self):
        self.name = None
        self.Base_Depth = None
        self.Type = None
        self.Created = None
        self.Modified = None
        self.Sample_id = None
        self.Label = None
    
    def parse(self, data):
        _, _, self.name = data.next()[:-1].split(" ", 2)
        _, _, _, self.Base_Depth = data.next().split(" ", 3)
        _, _, self.Type = data.next().split(" ", 2)
        _, _, self.Created = data.next().split(" ", 2)
        _, _, self.Modified = data.next().split(" ", 2)
        _, _, _, self.Sample_id = data.next().split(" ", 3)
        if self.Type != "LOG":
            _, _, self.Label = data.next().split(" ")
        return self

class Zone(object):
    def __init__(self):
        self.name = None
        self.Scheme_ID = None
        self.Top_sample = None
        self.Base_sample = None
        self.Top_sample_ID = None
        self.Base_sample_ID = None
        self.Separator = None
        self.Upper_unit = None
        self.Upper_boundary = None
        self.Lower_boundary = None
        self.Upper_questionable = None
        self.Lower_questionable = None
    
    def parse(self, data):
        _, _, self.name = data.next().split(" ", 2)
        _, _, _, self.Scheme_ID = data.next().split(" ", 3)
        _, _, _, self.Top_sample = data.next().split(" ", 3)
        _, _, _, self.Base_sample = data.next().split(" ", 3)
        _, _, _, _, self.Top_sample_ID = data.next().split(" ", 4)
        _, _, _, _, self.Base_sample_ID = data.next().split(" ", 4)
        _, _, self.Separator = data.next().split(" ", 2)
        _, _, _, self.Upper_unit = data.next().split(" ", 3)
        _, _, _, self.Upper_boundary = data.next().split(" ", 3)
        _, _, _, self.Lower_boundary = data.next().split(" ", 3)
        _, _, _, self.Upper_questionable = data.next().split(" ", 3)
        _, _, _, self.Lower_questionable = data.next().split(" ", 3)
        return self

class Interval(object):
    def __init__(self):
        self.Upper_depth = None
        self.Lower_depth = None
        self.Type = None
        self.content = None
        self.Modified = None
        self.Modifier = None
    
    def parse(self, data):
        _, self.Lower_depth, _, self.Upper_depth = data.next()[1:-2].split()
        _, _, self.Type = data.next().split(" ",2)
        if self.Type  == "Chronostratigraphy":
            self.content = Zone().parse(data)
        elif self.Type  == "Lithostratigraphy":
            self.content = Zone().parse(data)
        elif self.Type  == "Biozone":
            _, _, _, self.Biozone_data = data.next().split(" ",3)
            self.content = Zone().parse(data)
        _, _,self.Modified = data.next().split(" ",2)
        _, _,self.Modifier = data.next().split(" ",2)
        return self

class FileIterator(object):
    def __init__(self, data):
        self.i = 0
        self.data = data
        self.size = len(data)
    
    def has_next(self):
        return self.size > self.i
    
    def peek(self):
        return self.data[self.i]

    def next(self):
        self.i += 1
        return self.data[self.i-1].strip()

def make_interval_df(ls_interval):
    d = {
    "Upper_depth" : [interval.Upper_depth for interval in ls_interval ],
    "Lower_depth" : [interval.Lower_depth for interval in ls_interval ],
    "Type" : [interval.Type for interval in ls_interval ],
    "Modified" : [interval.Modified for interval in ls_interval ],
    "Modifier" : [interval.Modifier for interval in ls_interval ],
    "name" : [interval.content.name for interval in ls_interval ],
    "Scheme_ID" :  [interval.content.Scheme_ID for interval in ls_interval ],
    "Top_sample" :  [interval.content.Top_sample for interval in ls_interval ],
    "Base_sample" :  [interval.content.Base_sample for interval in ls_interval ],
    "Top_sample_ID" :  [interval.content.Top_sample_ID for interval in ls_interval ],
    "Base_sample_ID" :  [interval.content.Base_sample_ID for interval in ls_interval ],
    "Separator" :  [interval.content.Separator for interval in ls_interval ],
    "Upper_unit" :  [interval.content.Upper_unit for interval in ls_interval ],
    "Upper_boundary" :  [interval.content.Upper_boundary for interval in ls_interval ],
    "Lower_boundary" :  [interval.content.Lower_boundary for interval in ls_interval ],
    "Upper_questionable" :  [interval.content.Upper_questionable for interval in ls_interval ],
    "Lower_questionable" :  [interval.content.Lower_questionable for interval in ls_interval ]
    }
    df = pd.DataFrame(data=d)
    return df

def get_interval_df(fn):
    with open(fn) as f:
        data = FileIterator(f.readlines())

    list_of_intervals = []
    while(data.has_next()):
        if data.peek().split(" ")[0] == "[INTERVAL":
            new_interval = Interval().parse(data)
            list_of_intervals.append(new_interval)
        else:
            data.next()
    return make_interval_df(list_of_intervals)


def make_sample_df(ls_sampes):
    d = {
    "name" : [sample.name for sample in ls_sampes ],
    "Base_Depth" : [sample.Base_Depth for sample in ls_sampes ],
    "Type" : [sample.Type for sample in ls_sampes ],
    "Created" : [sample.Created for sample in ls_sampes ],
    "Modified" : [sample.Modified for sample in ls_sampes ],
    "Sample_id" : [sample.Sample_id for sample in ls_sampes ],
    "Label" : [sample.Label for sample in ls_sampes ]
    }
    return pd.DataFrame(data=d)

def get_sample_df(fn):
    with open(fn) as f:
        data = FileIterator(f.readlines())
    
    list_of_samples = []
    while(data.has_next()):
        if data.peek().split(" ")[0] == "[SAMPLE":
            list_of_samples.append(Sample().parse(data))
        else:
            data.next()
    return make_sample_df(list_of_samples)