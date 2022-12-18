checkpoint_config = dict(interval=9000)
log_config = dict(interval=100, hooks=[dict(type='TextLoggerHook'), dict(type='WandbLoggerHook',init_kwargs=dict(project='noise_label_analysis',name='zuoye_faster_rcnn_loc_error_50'))])
custom_hooks = [dict(type='NumClassCheckHook')]
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
opencv_num_threads = 0
mp_start_method = 'fork'
auto_scale_lr = dict(enable=False, base_batch_size=1)
work_dir = 'E:\\researchprojects\mmdetection\work_dirs'
auto_resume = False
