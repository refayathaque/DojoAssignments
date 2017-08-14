function findNumber(arr, k) {
    n = arr.length
    for (i = 0; i < n; i++) {
        var flag = 'Yes'
        if (arr[i] === k) {
            break;
        }
        else {
            flag = 'No'
            continue;
        }
    }
    return flag;
}

console.log(findNumber([1, 3, 3, 3, 5], 1));

function oddNumbers(l, r) {
    oddArr = [];
    for (i = l; i <= r; i ++) {
        if (i % 2 !== 0) {
            oddArr.push(i);
        }
    }
    return oddArr;
}

console.log(oddNumbers(6, 14));

console.log('---------------------------------------')

function fizzbuzz() {
    for(i = 1; i < 101; i++) {
        if(i % 3 === 0 && i % 5 === 0){
            console.log('fizzbuzz');
            continue;
        }
        if(i % 3 === 0){
            console.log('fizz');
            continue;
        }
        if(i % 5 === 0){
            console.log('buzz');
            continue;
        }
        else{
            console.log(i);
        }
    }
}

fizzbuzz();

console.log('---------------------------------------')

function fizzbuzz2() {
    for(i = 1; i <= 100; i++) {
        if(i % 3 === 0 && i % 5 === 0) {
            console.log('fizzbuzz')
            continue;
        }
        if(i % 3 === 0) {
            console.log('fizz')
            continue;
        }
        if(i % 5 === 0) {
            console.log('buzz')
            continue;
        }
        else {
            console.log(i);
        }
    }
}

fizzbuzz2();

console.log('---------------------------------------')

function fizzbuzz3() {
    for(i = 1; i <= 100; i++) {
        if(i % 3 === 0 && i % 5 === 0) {
            console.log('fizzbuzz')
            continue;
        }
        if(i % 3 === 0) {
            console.log('fizz')
            continue;
        }
        if(i % 5 === 0) {
            console.log('buzz')
            continue;
        }
        else {
            console.log(i);
        }
    }
}

fizzbuzz3();
