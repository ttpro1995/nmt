# -*- coding: utf-8 -*-
from comet_ml import Experiment


class SingletonObject:
  __instance = None

  @staticmethod
  def getInstance():
    """ Static access method. """
    if SingletonObject.__instance == None:
      SingletonObject()
    return SingletonObject.__instance

  def __init__(self, disabled=False):
    """ Virtually private constructor. """
    if SingletonObject.__instance != None:
      raise Exception("This class is a singleton!")
    else:
      SingletonObject.__instance = self
      self.init_comet(disabled)

  def init_comet(self, disabled):
    """
    init comet object
    :param disabled:
    :return:
    """
    self.comet_ml_experiment = Experiment(api_key="S3mM1eMq6NumMxk2QJAXASkUM",
               project_name="nmt", workspace="ttpro1995", auto_output_logging="simple",
               disabled=disabled)

  def get_comet_ml_experiment(self):
    return self.comet_ml_experiment

  def disable_comet(self):
    self.comet_ml_experiment.disable_mp()