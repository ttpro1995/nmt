from comet_ml import Experiment


class SingletonObject:
  __instance = None
  comet_ml_experiment = Experiment(api_key="S3mM1eMq6NumMxk2QJAXASkUM",
                          project_name="nmt", workspace="ttpro1995")

  @staticmethod
  def getInstance():
    """ Static access method. """
    if SingletonObject.__instance == None:
      SingletonObject()
    return SingletonObject.__instance

  def __init__(self):
    """ Virtually private constructor. """
    if SingletonObject.__instance != None:
      raise Exception("This class is a singleton!")
    else:
      SingletonObject.__instance = self

  def get_comet_ml_experiment(self):
    return self.comet_ml_experiment