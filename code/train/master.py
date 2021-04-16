from train import main
from config import model_names, datasets_ch, datasets_en
from config import experimental_dataset, experimental_model_name, epochs, batch_size, l2_param, lr_param
import time


# # Run all the models on all the datasets
# for experimental_dataset in datasets_ch + datasets_en:
#     for experimental_model_name in model_names:
#         print('================ [{}] ================'.format(
#             time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#         print('[Dataset]\t{}'.format(experimental_dataset))
#         print('[Model]\t{}'.format(experimental_model_name))
#         print()
#         print()
#         main(experimental_dataset, experimental_model_name,
#              epochs, batch_size, l2_param, lr_param)


# Run the specific model on the specific dataset
print('================ [{}] ================'.format(
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
print('[Dataset]\t{}'.format(experimental_dataset))
print('[Model]\t{}'.format(experimental_model_name))
print()
print('The hyparameters: ')
print('[Epoch]\t{}'.format(epochs))
print('[Batch Size]\t{}'.format(batch_size))
print('[L2 param]\t{}'.format(l2_param))
print('[Learning Rate]\t{}'.format(lr_param))
print()

main(experimental_dataset, experimental_model_name,
     epochs, batch_size, l2_param, lr_param)
