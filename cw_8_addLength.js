// write a function that takes a String and returns an Array/list with the length 
// of each word added to each element, separated by a space.

// Note: Input string will have at least one element; 
// words will always be separated by a space.

// addLength('apple ban') => ["apple 5", "ban 3"]
// addLength('you will win') => ["you 3", "will 4", "win 3"]

function addLength(str){
	var arrayOut = str.split(" ");
	var arrayLength = arrayOut.length;
	for (var i = 0; i < arrayLength; i++){
	arrayOut[i] = arrayOut[i].concat(" ".concat(arrayOut[i].length));
	}
	return arrayOut
}
