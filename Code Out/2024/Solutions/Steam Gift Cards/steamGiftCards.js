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
 * Complete the 'countValid' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING_ARRAY codes
 */

function countValid(n, codes) {
    let count = 0;
    for (const s of codes) {
        let split = s.split('.');
        if (!split[0]) {
            count++;
            continue;
        }
        if (split[0].length == split[1].length) {
            count += split[0] == split[1];
            continue;
        }
        let queue = {};
        for (const v in split[0])
            queue[v] = split[0][v];
        let front = 0; let back = split[0].length;
        for (const char of split[1]) {
            if (char == queue[front])
                delete queue[front++];
            if (!(back - front)) {
                count++;
                break;
            }
        }
    }
    console.log(count);
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    let codes = [];

    for (let i = 0; i < n; i++) {
        const codesItem = readLine();
        codes.push(codesItem);
    }

    countValid(n, codes);
}