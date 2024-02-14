from django.shortcuts import render
def flight(request):
    if(request.method=="POST"):
        data=request.POST #store all the val of txtboxs
        neo=data.get('neo')
        onekm=data.get('onekm')
        pha=data.get('pha')
        absolmag=data.get('absolmag')
        sloppara=data.get('sloppara')
        numbsobs=data.get('numbsobs')
        rmsresi=data.get('rmsresi')
        uncerpara=data.get('uncerpara')
        epoch=data.get('epoch')
        meanano=data.get('meanano')
        arguperi=data.get('arguperi')
        node=data.get('node')
        ecliptic=data.get('ecliptic')
        eccentricity=data.get('eccentricity')
        meanmotion=data.get('meanmotion')
        axis=data.get('axis')
        numops=data.get('numops')
        tp=data.get('tp')
        orbitalperiod=data.get('orbitalperiod')
        peridist=data.get('peridist')
        aphedist=data.get('aphedist')
        semirectum=data.get('semirectum')
        synoperiod=data.get('synoperiod')
        synoperiod1=data.get('synoperiod1')
        synoperiod2=data.get('synoperiod2')
        if('buttonflo' in request.POST):
            import pandas as pd
            path="C:\\Users\\umraf\\OneDrive\\Desktop\\batch4\\Data\\Data\\afs.csv"
            data=pd.read_csv(path)
            inputs=data.drop(['satisfaction'],axis=1)
            output=data['satisfaction']
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            from sklearn.preprocessing import StandardScaler
            sc=StandardScaler()
            x_train=sc.fit_transform(x_train)
            x_test=sc.transform(x_test)
            from sklearn.svm import SVC
            model=SVC()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            from sklearn.metrics import accuracy_score
            acc=accuracy_score(y_test,y_pred)*100
            import numpy as np
            newip=np.array([[neo,onekm,pha,absolmag,sloppara,numbsobs,rmsresi,uncerpara,epoch,meanano,arguperi,node,ecliptic,eccentricity,meanmotion,axis,numops,tp,orbitalperiod,peridist,aphedist,semirectum,synoperiod,synoperiod1,synoperiod2]])
            newip=sc.transform(newip)
            result=model.predict(newip)
            
            return render(request,"flight.html",context={'result':result})

    return render(request,'flight.html')