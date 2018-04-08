#####################
#Discard List format
#####################
#For each number of allowed discarded cards and required card for that value the format is
#(NumOfCards,FaceName)
#FaceName can be a wild card * = any card or no validation
#If you cannot discard more or less than 2 your list would be [(0,'*'),(2,'*')]
###################
#Array List format
###################
#value:suit
#Value can be a wild card # = any number, r = any face, * = any value
#Value can also be a specific value 1 - 15
#suit can be a wild card * = any suit, f = any face
#suit can also be a specific suit or face name
class Rules:
    def getRule(this, rule):
        r = rule.lower()
        if r == "old republic":
            return {'faces': {'Idiot':0,
                              'Rancor':9,
                              'Jedi Knight':3,
                              'Jedi Master':3,
                              'Dark Jedi':-14, 
                              'Lord of the Sith':10,
                              'Smuggler':10, 
                              'Bounty Hunter':9
                             },
                    'discardList': {0:'*', 1:'*', 2:'*', 3:'Jedi Master',4:'Jedi Master'},
                    'array':{'name':"Jedi's", 'cards':['*:Jedi Knight', '*:Jedi Master', '#:Saber']}
            }
        elif r == "rebel alliance":
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':3,
                              'Jedi Master':4,
                              'Dark Jedi':12, 
                              'Lord of the Sith':-10,
                              'Smuggler':5, 
                              'Bounty Hunter':9
                             },
                    'discardList':{0,'*', 1:'*', 2:'*', 3:'*'},
                    'array':{'name':'Force', 'cards':['*:Jedi Knight', '*:Jedi Knight', '15:*']}
            }
        elif r == "new republic":
            return {'faces': {'Idiot':0,
                              'Rancor':8,
                              'Jedi Knight':4,
                              'Jedi Master':3,
                              'Dark Jedi':12, 
                              'Lord of the Sith':-11,
                              'Smuggler':4, 
                              'Bounty Hunter':10
                             },
                    'discardList':{0:'*', 1:'*', 3:'*'},
                    'array':{'name':"Republic's", 'cards':['*:Jedi Knight', '*:Jedi Master', '*:Smuggler']}
            }
        elif r == "imperial":
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':15,
                              'Jedi Master':-9,
                              'Dark Jedi':3, 
                              'Lord of the Sith':4,
                              'Smuggler':7, 
                              'Bounty Hunter':3
                             },
                    'discardList': 0:'*', 2:'*',
                    'array':{'name':"Sith", 'cards':['*:Lord of the Sith', '*:Commander', '15:*']}
            }
        elif r == "cloud city casino":
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':4,
                              'Jedi Master':6,
                              'Dark Jedi':9, 
                              'Lord of the Sith':-8,
                              'Smuggler':5, 
                              'Bounty Hunter':7
                             },
                    'discardList':{0:'*', 2:'*', 4:'*'},
                    'array':{'name':'Partnership', 'cards':['*:Jedi Knight', '*:Smuggler', '*:Smuggler']}
            }
        elif r == "mos eisley":
            return {'faces': {'Idiot':0,
                              'Rancor':5,
                              'Jedi Knight':7,
                              'Jedi Master':8,
                              'Dark Jedi':-11, 
                              'Lord of the Sith':10,
                              'Smuggler':6, 
                              'Bounty Hunter':5
                             },
                    'discardList':{0:'*', 1:'*', 4:'Bounty Hunter', 4:'Smuggler'},
                    'array':{'name':'Force', 'cards':['*:Smuggler', '*:Bounty Hunter', '#:Coin']}
            }        
        elif r == "corellian":
            return {'faces': {'Idiot':0,
                              'Rancor':4,
                              'Jedi Knight':10,
                              'Jedi Master':-13,
                              'Dark Jedi':11, 
                              'Lord of the Sith':11,
                              'Smuggler':4, 
                              'Bounty Hunter':3
                             },
                    'discardList':{0:'*', 2:'*', 3:'*', 4:'*'},
                    'array':{'name':"Smuggler's", 'cards':['*:Smuggler', '*:Smugler', '#:Coin']}
            }        
        elif r == "corporate sector":
            return {'faces': {'Idiot':0,
                              'Rancor':5,
                              'Jedi Knight':-7,
                              'Jedi Master':8,
                              'Dark Jedi':7, 
                              'Lord of the Sith':8,
                              'Smuggler':6, 
                              'Bounty Hunter':3
                             },
                    'discardList':{0:'*', 3:'*'},
                    'array':{'name':"Hunter's", 'cards':['*:Bounty Hunter', '*:Bounty Hunter', '#:Coin']}
            }        
        elif r == "crseih station":
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':8,
                              'Jedi Master':-6,
                              'Dark Jedi':5, 
                              'Lord of the Sith':4,
                              'Smuggler':6, 
                              'Bounty Hunter':6
                             },
                    'discardList':{0:'*', 1:'*',2:'*'},
                    'array':{'name':'Force', 'cards':['*:Flask', '*:Flask', '*:Flask', '*:Flask']}
            }        
        else:
            return {'faces': {'Idiot':0,
                              'Rancor':9,
                              'Jedi Knight':3,
                              'Jedi Master':3,
                              'Dark Jedi':-14, 
                              'Lord of the Sith':10,
                              'Smuggler':10, 
                              'Bounty Hunter':9
                             },
                    'discardList':{0:'*', 1:'*', 2:'*', 3:'Jedi Master',4:'Jedi Master'},
                    'array':{'name':"Idiot's", 'cards':['*:Idiot', '2:*', '3:*']}
            }       
# class Rules:
#     def getRule(this, rule):
#         r = rule.lower()
#         if r == "old republic":
#             return {'faces': {'Idiot':0,
#                               'Rancor':9,
#                               'Jedi Knight':3,
#                               'Jedi Master':3,
#                               'Dark Jedi':-14, 
#                               'Lord of the Sith':10,
#                               'Smuggler':10, 
#                               'Bounty Hunter':9
#                              },
#                     'discardList': [(0,'*'), (1,'*'), (2,'*'), (3,'Jedi Master')(4,'Jedi Master')],
#                     'array':{'name':"Jedi's", 'cards':['*:Jedi Knight', '*:Jedi Master', '#:Saber']}
#             }
#         elif r == "rebel alliance":
#             return {'faces': {'Idiot':0,
#                               'Rancor':7,
#                               'Jedi Knight':3,
#                               'Jedi Master':4,
#                               'Dark Jedi':12, 
#                               'Lord of the Sith':-10,
#                               'Smuggler':5, 
#                               'Bounty Hunter':9
#                              },
#                     'discardList':[(0,'*'), (1,'*'), (2,'*'), (3,'*')],
#                     'array':{'name':'Force', 'cards':['*:Jedi Knight', '*:Jedi Knight', '15:*']}
#             }
#         elif r == "new republic":
#             return {'faces': {'Idiot':0,
#                               'Rancor':8,
#                               'Jedi Knight':4,
#                               'Jedi Master':3,
#                               'Dark Jedi':12, 
#                               'Lord of the Sith':-11,
#                               'Smuggler':4, 
#                               'Bounty Hunter':10
#                              },
#                     'discardList':[(0,'*'), (1,'*'), (3,'*')],
#                     'array':{'name':"Republic's", 'cards':['*:Jedi Knight', '*:Jedi Master', '*:Smuggler']}
#             }
#         elif r == "imperial":
#             return {'faces': {'Idiot':0,
#                               'Rancor':7,
#                               'Jedi Knight':15,
#                               'Jedi Master':-9,
#                               'Dark Jedi':3, 
#                               'Lord of the Sith':4,
#                               'Smuggler':7, 
#                               'Bounty Hunter':3
#                              },
#                     'discardList': [(0,'*'), (2,'*')],
#                     'array':{'name':"Sith", 'cards':['*:Lord of the Sith', '*:Commander', '15:*']}
#             }
#         elif r == "cloud city casino":
#             return {'faces': {'Idiot':0,
#                               'Rancor':7,
#                               'Jedi Knight':4,
#                               'Jedi Master':6,
#                               'Dark Jedi':9, 
#                               'Lord of the Sith':-8,
#                               'Smuggler':5, 
#                               'Bounty Hunter':7
#                              },
#                     'discardList':[(0,'*'), (2,'*'), (4,'*')],
#                     'array':{'name':'Partnership', 'cards':['*:Jedi Knight', '*:Smuggler', '*:Smuggler']}
#             }
#         elif r == "mos eisley":
#             return {'faces': {'Idiot':0,
#                               'Rancor':5,
#                               'Jedi Knight':7,
#                               'Jedi Master':8,
#                               'Dark Jedi':-11, 
#                               'Lord of the Sith':10,
#                               'Smuggler':6, 
#                               'Bounty Hunter':5
#                              },
#                     'discardList':[(0,'*'), (1,'*'), (4,'Bounty Hunter'), (4,'Smuggler')],
#                     'array':{'name':'Force', 'cards':['*:Smuggler', '*:Bounty Hunter', '#:Coin']}
#             }        
#         elif r == "corellian":
#             return {'faces': {'Idiot':0,
#                               'Rancor':4,
#                               'Jedi Knight':10,
#                               'Jedi Master':-13,
#                               'Dark Jedi':11, 
#                               'Lord of the Sith':11,
#                               'Smuggler':4, 
#                               'Bounty Hunter':3
#                              },
#                     'discardList':[(0,'*'), (2,'*'), (3,'*'), (4,'*')],
#                     'array':{'name':"Smuggler's", 'cards':['*:Smuggler', '*:Smugler', '#:Coin']}
#             }        
#         elif r == "corporate sector":
#             return {'faces': {'Idiot':0,
#                               'Rancor':5,
#                               'Jedi Knight':-7,
#                               'Jedi Master':8,
#                               'Dark Jedi':7, 
#                               'Lord of the Sith':8,
#                               'Smuggler':6, 
#                               'Bounty Hunter':3
#                              },
#                     'discardList':[(0,'*'), (3,'*')],
#                     'array':{'name':"Hunter's", 'cards':['*:Bounty Hunter', '*:Bounty Hunter', '#:Coin']}
#             }        
#         elif r == "crseih station":
#             return {'faces': {'Idiot':0,
#                               'Rancor':7,
#                               'Jedi Knight':8,
#                               'Jedi Master':-6,
#                               'Dark Jedi':5, 
#                               'Lord of the Sith':4,
#                               'Smuggler':6, 
#                               'Bounty Hunter':6
#                              },
#                     'discardList':[(0,'*'), (1,'*'),(2,'*')],
#                     'array':{'name':'Force', 'cards':['*:Flask', '*:Flask', '*:Flask', '*:Flask']}
#             }        
#         else:
#             return {'faces': {'Idiot':0,
#                               'Rancor':9,
#                               'Jedi Knight':3,
#                               'Jedi Master':3,
#                               'Dark Jedi':-14, 
#                               'Lord of the Sith':10,
#                               'Smuggler':10, 
#                               'Bounty Hunter':9
#                              },
#                     'discardList':[(0,'*'), (1,'*'), (2,'*'), (3,'Jedi Master'),(4,'Jedi Master')],
#                     'array':{'name':"Idiot's", 'cards':['*:Idiot', '2:*', '3:*']}
#             }
# class RulesCompressed:
#     ruleDict = {"old republic": {'faces': {'Idiot':0, 'Rancor':9, 'Jedi Knight':3, 'Jedi Master':3, 'Dark Jedi':-14, 'Lord of the Sith':10, 'Smuggler'10:, 'Bounty Hunter':9},
#             'discardList': [(0,'*'), (1,'*'), (2,'*'), (3,'Jedi Master')(4,'Jedi Master')], 'array':{'name':"Jedi's", 'cards':['*:Jedi Knight', '*:Jedi Master', '#:Saber']}},
#             "rebel alliance": {'faces': {'Idiot':0, 'Rancor':7, 'Jedi Knight':3, 'Jedi Master':4, 'Dark Jedi':12, 'Lord of the Sith':-10, 'Smuggler':5, 'Bounty Hunter':9},
#             'discardList':[(0,'*'), (1,'*'), (2,'*'), (3,'*')], 'array':{'name':'Force', 'cards':['*:Jedi Knight', '*:Jedi Knight', '15:*']}},
#             "new republic":{ 'faces': {'Idiot':0, 'Rancor':8, 'Jedi Knight':4, 'Jedi Master':3, 'Dark Jedi':12, 'Lord of the Sith':-11, 'Smuggler':4, 'Bounty Hunter':10},
#             'discardList':[(0,'*'), (1,'*'), (3,'*')], 'array':{'name':"Republic's", 'cards':['*:Jedi Knight', '*:Jedi Master', '*:Smuggler']}},
#             "imperial": {'faces': {'Idiot':0, 'Rancor':7, 'Jedi Knight':15, 'Jedi Master':-9, 'Dark Jedi':3, 'Lord of the Sith':4, 'Smuggler':7, 'Bounty Hunter':3},
#             'discardList': [(0,'*'), (2,'*')], 'array':{'name':"Sith", 'cards':['*:Lord of the Sith', '*:Commander', '15:*']}},
#             "cloud city casino": {'faces': {'Idiot':0, 'Rancor':7, 'Jedi Knight':4, 'Jedi Master':6, 'Dark Jedi':9, 'Lord of the Sith':-8, 'Smuggler':5, 'Bounty Hunter':7},
#             'discardList':[(0,'*'), (2,'*'), (4,'*')], 'array':{'name':'Partnership', 'cards':['*:Jedi Knight', '*:Smuggler', '*:Smuggler']}},
#             "mos eisley": {'faces': {'Idiot':0, 'Rancor':5, 'Jedi Knight':7, 'Jedi Master':8, 'Dark Jedi':-11, 'Lord of the Sith':10, 'Smuggler':6, 'Bounty Hunter':5},
#             'discardList':[(0,'*'), (1,'*'), (4,'Bounty Hunter'), (4,'Smuggler')], 'array':{'name':'Force', 'cards':['*:Smuggler', '*:Bounty Hunter', '#:Coin']}},        
#             "corellian": {'faces': {'Idiot':0, 'Rancor':4, 'Jedi Knight':10, 'Jedi Master':-13, 'Dark Jedi':11, 'Lord of the Sith':11, 'Smuggler':4, 'Bounty Hunter':3},
#             'discardList':[(0,'*'), (2,'*'), (3,'*'), (4,'*')], 'array':{'name':"Smuggler's", 'cards':['*:Smuggler', '*:Smugler', '#:Coin']}},        
#             "corporate sector": {'faces': {'Idiot':0, 'Rancor':5, 'Jedi Knight':-7, 'Jedi Master':8, 'Dark Jedi':7, 'Lord of the Sith':8, 'Smuggler':6, 'Bounty Hunter':3},
#             'discardList':[(0,'*'), (3,'*')], 'array':{'name':"Hunter's", 'cards':['*:Bounty Hunter', '*:Bounty Hunter', '#:Coin']}},        
#             "crseih station": {'faces': {'Idiot':0, 'Rancor':7, 'Jedi Knight':8, 'Jedi Master':-6, 'Dark Jedi':5, 'Lord of the Sith':4, 'Smuggler':6, 'Bounty Hunter':6},
#             'discardList':[(0,'*'), (1,'*'),(2,'*')], 'array':{'name':'Force', 'cards':['*:Flask', '*:Flask', '*:Flask', '*:Flask']}}} 

#     def getRule(this, rule):
#         r = rule.lower()       
#         if  not r in ruleDict.keys():
#             return {'faces': {'Idiot':0, 'Rancor':9, 'Jedi Knight':3, 'Jedi Master':3, 'Dark Jedi':-14, 'Lord of the Sith':10, 'Smuggler'10:, 'Bounty Hunter':9},
#                     'discardList':[(0,'*'), (1,'*'), (2,'*'), (3,'Jedi Master')(4,'Jedi Master')], 'array':{'name':"Idiot's", 'cards':['*:Idiot', '2:*', '3:*']}}
#         else:
#             return this.ruleDict[r]