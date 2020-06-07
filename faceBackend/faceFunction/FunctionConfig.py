class FunctionConfig:
	EmotionRecConfig={'supportEmotion':['Angry','Happy','Surprise','Neutral'],
	                  'numTimeLimit':30,
		                'recgFrameInterval':15}
	ImageQualAssConfig={'modelPath':'/media/tsz/Data/Work/Tracking/GithubProject/No-Reference-Image-Quality-Assessment-using-BRISQUE-Model/Python/libsvm/python/allmodel'}

	# 想把所欧子类的参数统一为config，但是不确定这是否意味着更幼的选择 - 将参数直接放在函数参数意味着更加确定明显（尤其在补全时），放在dict中意味着更加不确定（虽然带来的可变性更大）
	# @staticmethod
	# def getFaceTrackerInitConfigDefaultDict():
	# 	d={}
	# 	d.setdefault('wantIDs',None)
	# 	d.setdefault('use_scale',True)
	# 	d.setdefault('scale_xy',0.25)
	# 	return d