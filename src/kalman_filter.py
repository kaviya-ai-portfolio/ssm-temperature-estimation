# import numpy for math calculations
import numpy as np


class KalmanFilter:
    def __init__(self):
        # initial estimated temperature (start guess)
        self.estimated_temperature = 20.0

        # initial uncertainty (how unsure we are)
        self.estimate_uncertainty = 1.0

        # process noise (how much temperature can change)
        self.process_noise = 0.01

        # measurement noise (sensor noise level)
        self.measurement_noise = 0.5

    def update(self, measured_temperature):
        """
        Update step of Kalman Filter
        Takes one noisy measurement
        Returns filtered temperature
        """

        # prediction step:
        # we assume temperature stays almost the same
        predicted_temperature = self.estimated_temperature
        predicted_uncertainty = self.estimate_uncertainty + self.process_noise

        # calculate Kalman Gain
        # this decides how much we trust new measurement
        kalman_gain = predicted_uncertainty / (
            predicted_uncertainty + self.measurement_noise
        )

        # update estimated temperature using measurement
        self.estimated_temperature = predicted_temperature + (
            kalman_gain * (measured_temperature - predicted_temperature)
        )

        # update uncertainty
        self.estimate_uncertainty = (1 - kalman_gain) * predicted_uncertainty

        # return filtered temperature
        return self.estimated_temperature
