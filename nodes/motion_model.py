import robot_pose
import prob_utilities
import math

class motion_model:
	def __init__(self):
		# alpha1 = 0.05 meters/meter
		# alpha2 = 0.001 meters/degree
		# alpha3 = 5 degrees/meter
		# alpha4 = 0.05 degrees/degree

	def update_motion(self, old_particle, cur_coords, cur_theta):
		# break up old particle
		old_x = old_particle.pose[0]
		old_y = old_particle.pose[1]
		old_theta - old_particle[2]
		#break up current pose
		cur_x = cur_coords[0]
		cur_y = cur_coords[1]
		# we are passed cur_theta
		# odometry
		trans = sqrt((cur_x - old_x)**2 + (cur_y - old_y)**2)
		rot1 = atan2(cur_y - old_y, cur_x - old_x) - old_theta
		rot2 = cur_theta - old_theta - rot1
		# noise
		n_rot1 = rot1 + random.gauss(0.0,0.3)
		n_trans = trans + random.gauss(0.0,0.1)
		n_rot2 = rot2 + random.gauss(0.0,0.3)
		# normal distribution (zero-centered)
		p1 = prob_normal_dist(rot1 - n_rot1, 0.05*abs(n_rot1)+0.001*n_trans)
		p2 = prob_normal_dist(trans - n_trans, 5*n_trans+0.05(abs(n_rot1)+abs(n_rot2)))
		p3 = prob_normal_dist(rot2 - n_rot2, 0.05*abs(n_rot2)+0.001*n_trans)

		return p1*p2*p3

	def prob_normal_dist(self, a, b):
		# normal distribution (zero-centered)
		return (1/mqth.sqrt(2*math.pi*b**2))**(-((a**2)/(2*b**2)))