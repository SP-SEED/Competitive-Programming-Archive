'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countHits' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER r
 *  3. INTEGER a
 *  4. INTEGER b
 *  5. INTEGER_ARRAY x
 *  6. INTEGER_ARRAY y
 */

function countHits(n, r, a, b, x, y) {
    let count = 0;
    let i = x.length;
    while (i) {
        if (Math.sqrt((x[--i] - a)**2 + (y[i] - b)**2) <= r)
            count++;
    }
    console.log(count);
}

function main() {
    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const r = parseInt(firstMultipleInput[1], 10);

    const secondMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const a = parseInt(secondMultipleInput[0], 10);

    const b = parseInt(secondMultipleInput[1], 10);

    const x = readLine().replace(/\s+$/g, '').split(' ').map(xTemp => parseInt(xTemp, 10));

    const y = readLine().replace(/\s+$/g, '').split(' ').map(yTemp => parseInt(yTemp, 10));

    countHits(n, r, a, b, x, y);
}
