test(){
    pytest -v --ignore=./lib/ --ignore=./lib64/
}

virt(){
    source ./bin/activate.sh
}

if [[ -n $1 ]]; then
    if [[ $1 == 'test' ]]; then
        test
    elif [[ $1 == 'virt' ]]; then
        virt
    else
        echo 'Usage: ./run.sh [test || virt]'
    fi
elif [[ -z $1 ]]; then
    echo 'Command is required'
fi