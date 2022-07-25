// Given two strings, determine if they share a common substring. A substring may be as small as one character.

// Dadas dos cadenas, determine si comparten una subcadena común. Una subcadena puede ser tan pequeña como un carácter.

function twoStrings(s1, s2) {
	// Write your code here
	let hash = {};

	for (let i = 0; i < s1.length; i++) {
		hash[s1[i]] = (hash[s1[i]] || 0) + 1;
	}

	for (let i = 0; i < s2.length; i++) {
		if (hash.hasOwnProperty(s2[i])) return 'YES';
	}

	return 'NO';
}

twoStrings('hamaca', 'hamacaa');
