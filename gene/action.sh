# local shell
export ESC_ID=i-2ze3nt8kraa5usrfcn61
export set ESC_NAME=ali_ecs

cat /root/.ssh/id_rsa.pub | ssh root@$ESC_NAME 'mkdir -p .ssh; cat >> .ssh/authorized_keys'

# config for osscmd 
# scp /root/.osscredentials root@$ESC_NAME:/root

# config for ossfs
scp /etc/passwd-ossfs root@$ESC_NAME:/etc

# worker shell
scp /root/remoteAction.sh root@$ESC_NAME:/root

echo "start at $(date +%Y-%m-%d_%H:%M:%S)"
export START=$(date +%s)
echo -------------------------
ssh root@$ESC_NAME 'chmod +x /root/remoteAction.sh; /root/remoteAction.sh'
echo -----stopping  $ESC_ID  --------------------
aliyuncli ecs StopInstance --InstanceId $ESC_ID
sleep 120
echo -----deleting  $ESC_ID  --------------------
aliyuncli ecs DeleteInstance --InstanceId $ESC_ID
sleep 30
echo "stop at $(date +%Y-%m-%d_%H:%M:%S)"
echo "spent $[($(date +%s)- $START)/3600+1] hours"

echo -----show  $ESC_ID, expect error  --------------------
aliyuncli ecs DescribeInstanceAttribute --InstanceId $ESC_ID