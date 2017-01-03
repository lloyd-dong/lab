# local shell
export ESC_ID=i-xxxxxxxxx
export set ESC_NAME=ali_ecs

cat /root/.ssh/id_rsa.pub | ssh root@$ESC_NAME 'mkdir -p .ssh; cat >> .ssh/authorized_keys'

# config for osscmd 
# scp /root/.osscredentials root@$ESC_NAME:/root

# config for ossfs
scp /etc/passwd-ossfs root@$ESC_NAME:/etc

# worker shell
scp /root/remoteAction.sh root@$ESC_NAME:/root
echo $(hostname)
echo -------------------------
ssh root@$ESC_NAME 'chmod +x /root/remoteAction.sh; /root/remoteAction.sh'
echo -------------------------
aliyuncli ecs StopInstance --InstanceId $ESC_ID
sleep 60
aliyuncli ecs DeleteInstance --InstanceId $ESC_ID 
sleep 10
aliyuncli ecs DescribeInstanceAttribute --InstanceId $ESC_ID