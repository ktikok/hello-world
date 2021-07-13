
import h5py
import numpy as np

#data=[]

#difference=[]

#for k in range(0,10):

old_which_event=[315, 456, 461, 752, 1201, 1825, 1969, 3253, 3407, 3603, 3923, 4011, 4479, 4873, 5442, 6175, 6347, 7356, 7425, 7508, 7572, 7745, 7973, 8304, 8996, 9382, 10288, 10576, 10781, 11852, 11890, 12020, 12218, 13356, 13607, 13692, 13752, 15012, 15648, 15703, 15884, 16747, 16836, 17267, 17408, 17413, 17704, 18097, 18721, 19956, 20110, 20306, 20525, 20613, 21007, 21401, 21861, 22489, 22661, 23592, 23661, 23744, 23808, 23981, 24209, 25131, 25444, 25872, 26411, 27402, 27410, 27855, 28235, 28258, 28543, 28667, 29570, 30598, 30978, 31308, 31660, 32255, 33374, 33499, 34392, 34568, 35532, 35684, 35802, 35967, 36978, 37250, 38190, 39257, 39446, 39450, 39476, 42592, 43172, 43647, 43664, 43850, 44530, 44966, 45376]

o_w_e_s=[]


new_images=[]
new_where=[]
for i in range(10):
  new=h5py.File('/home/swkim/test_makeDetectorImage/trackpt_hdf5_32PU_224x224/QCDBkg/HT1000to1500/qcd1000to1500_'+str(i)+'.h5','r')
  new_images.append(new['all_events']['images'])
  
new_where.append(np.where(new_images[0][0,0]>0))

#print(new_where[0][0])
#raise

old_images=[]
for i in range(1,13):
  old=h5py.File('/home/swkim/HEP-CNN_newest/HEP-CNN/data/trackpt_hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(i)+'.h5','r')
  #difference.append(['new=qcd1000to1500_'+str(i)+'.h5 old='+'data_'+str(i)+'.h5'])
  #difference.append(['new_start','new_end','old-new'])
  
  old_images.append(old['all_events']['images'])
  #print('old=',l)


print('start')

print(len(new_where[0][1]))

def FindMyLocation():
  nwl=len(new_where[0][1])
  for l in range(nwl):
    for i in range(10):
      print(i)
      where_exact=np.where(old_images[i][:,0]== 
              new_images[0][0,0,new_where[0][0][l],new_where[0][1][l]]
                          )
      if len(where_exact[0]>0):
        print(where_exact)
  #print(nwl)
  '''
  for l in range(nwl):
    print('refference',l)
    print(np.where(new_images[5][:,0]== 
          new_images[file_num][0,0,new_where[0][0][l],new_where[0][1][l]]
                  )
          )
    
    print('new_file =',k, 'event =',0,
      'where = (',new_where[0][0][l],new_where[0][1][l],')',
      new_images[file_num][0,0,new_where[0][0][l],new_where[0][1][l]]
      )  
    print('old_file =',j+1,'event =',i,
      'where = (',where_exact[0][0],where_exact[1][0],')',
      old_images[j][i,0,where_exact[0][0],where_exact[1][0]]
      )
    print("")
  '''
#FindMyLocation()

'''
for i in range(10):
  print('file_num',i)
  print(np.where(new_images[i][:,0]== 
           new_images[file_num][0,0,new_where[0][0][l],new_where[0][1][l]])
  print(np.where(new_images[i][:,0]== 
           new_images[file_num][0,0,new_where[0][0][l],new_where[0][1][l]])
'''

    


def find_location(file_num):
  print(new_where)
  nwl=len(new_where[0][1])
  print(nwl)
  for l in range(nwl):
    print(l)
    for j in range(0,12):
      #print(j)
      for i in range(4096):
        if j==11 and i==518:
            break
      
        where_exact=np.where(old_images[j][i,0]==1000*new_images[file_num][0,0,new_where[0][0][l],new_where[0][1][l]])
        if len(where_exact[0])>0:
        #elif(new_images[5][0,0]*1000==old_images[j][i,0]).all():
          print('new_file =',k, 'event =',0,
                'where = (',new_where[0][0][l],new_where[0][1][l],')',
                new_images[file_num][0,0,new_where[0][0][l],new_where[0][1][l]]
                )  
          print('old_file =',j+1,'event =',i,
                'where = (',where_exact[0][0],where_exact[1][0],')',
                old_images[j][i,0,where_exact[0][0],where_exact[1][0]]
                )
          print("")
          break      
          
      #if 
#find_location(5)
  
      
    
def o_w_e_s():  
  for i in old_which_event:
    print(i)
    a=i//4096
    b=i%4096
    print(a)
    print(b)
    old_where=np.where(old_images[a][b,0]>0)
    
    print(old_where)
    print(new_where[0]==old_where[0])
    
    print((0 in (old_images[0])).any())
    break
    print(old_images[a][b,0]==new_images(0,0,new_where[0][0],new_where[1][0]))
    break
    #if (new_where_len+10>=old_where_len>=new_where_len-10):
    if ((new_where==old_where).all()):
      print(i,end=" ")
        
        #old_which_event.append(i+4096*(l-1))
  
  
    #'''

class new_or_old:
  def __init__(self):

    self.where=np.where(new_images[0,0]>0)
    self.where_len=len(np.where(new_images[0,0]>0)[0])
    #print(new_where)
    for i in range(new_where_len):
      print(new_images[0,0,new_where[0][i],new_where[1][i]])
  ''' 
    old_where=np.where(old_images[0,0]>0)
    old_where_len=len(np.where(old_images[0,0]>0)[0])
    #print(new_where)
    for i in range(old_where_len):
        print(old_images[0,0,old_where[0][i],old_where[1][i]])
  #print(len(np.where(old_images[0,0]>0)[0]))
  #'''

def find_old_which_event():
  for i in range(4096):
    if l==12 and i==518:
      break
    old_where_len=len(np.where(old_images[i,0]>0)[0])
    #if (new_where_len+10>=old_where_len>=new_where_len-10):
    if (new_where_len==old_where_len):
      #print('which_event=',i,'how_many=',old_where_len,end=" ")
      #print(i,end=" ")
      old_which_event.append(i+4096*(l-1))
  print("")
  print("###################################################3")
  print("")
  #'''
  print(old_which_event)