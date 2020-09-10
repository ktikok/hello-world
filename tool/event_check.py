import h5py

for i in range(1,12):
	d=h5py.File('/xrootd/store/user/jiwoong/HEP_CNN_Large_Image/hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(i)+'.h5', 'r')
	#d=h5py.File('/xrootd/store/user/hnam/sample4Nurion/2018DAS/Delphes/presel/hdf5_32PU_224x224/RPV/Gluino1400GeV/0000/RPV_1400-'+str(i)+'.h5', 'r')
  	
	print('noPU_224_train_'+str(i)+'.h5')
	print('images ',len(d['all_events']['images']),'labels ',len(d['all_events']['labels']),'weights ',len(d['all_events']['weights']))
#print(str(d.keys()))
#if (
#for i in str(d.keys):
 # print(i)

#d['all_event'].keys()

