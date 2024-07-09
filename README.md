# Candy Factory

Play book og the demo

Start a Redpanda cluster with a single broker
```
rpk container start -n 1
rpk topic create candies
rpk topic create retail-candies
```

Enable data transforms
```
rpk cluster config set data_transforms_enabled true
rpk container stop
rpk container start
```

Run the Wonka application to produce candies
```
cd factory
source env/bin/activate
pip install -r requirements.txt 
python3 wonka.py 
```

#rpk transform init goldenticket
Build and deploy the Golden ticket 
```
cd goldenticket 
rpk transform build
rpk transform deploy -i candies -o retail-candies
```

#rpk connect create -s kafka_franz//switch
Run the winning distribution pipeline
```
rpk topic create win
rpk topic create try-again
cd reconnect
rpk connect run demo.yaml
``` 



