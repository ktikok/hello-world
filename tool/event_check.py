import h5py

for i in range(1,33):
  #d=h5py.File('/users/tongilkim/work/data/noPU_224/noPU_224_train_'+str(i)+'.h5', 'r')
  d=h5py.File('/users/tongilkim/work/data/noPU_224/noPU_224_train_'+str(i)+'.h5', 'r')
  print('noPU_224_train_'+str(i)+'.h5')
  print('images ',len(d['all_events']['images']),'labels ',len(d['all_events']['labels']),'weights ',len(d['all_events']['weights']))
#print(str(d.keys()))
#if (
#for i in str(d.keys):
 # print(i)

#d['all_event'].keys()

