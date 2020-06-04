class libConfig:
	facialRecConfig={'modelPath':'/media/tsz/Data/Work/Tracking/GithubProject/Facial-Expression-Recognition.Pytorch/FER2013_VGG19/PrivateTest_model.t7',
	                 'net':'VGG19'}
	siamTrackerConfig={'pysotRoot':'/media/tsz/Data/Work/Tracking/Library/pysot',
						'modelRoot': '/media/tsz/Data/Work/Tracking/Library/pysot/experiments',
						'modelType':'siamrpn_alex_dwxcorr',
	                   'configBaseName':'config.yaml',
	                   'modelBaseName':'model.pth'}
	personDetConfig={'mmdetRoot':'/media/tsz/Data/Work/Tracking/Library/mmdetection',
	                 'configFile':'configs/faster_rcnn_r50_fpn_1x.py',
	                 'checkpoint':'checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth',}