// Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

// Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

// Harold es un secuestrador que escribió una nota de rescate, pero ahora le preocupa que se pueda rastrear hasta él a través de su letra. Encontró una revista y quiere saber si puede recortar palabras completas y usarlas para crear una réplica imposible de rastrear de su nota de rescate. Las palabras en su nota distinguen entre mayúsculas y minúsculas y debe usar solo palabras completas disponibles en la revista. No puede usar subcadenas o concatenaciones para crear las palabras que necesita.

// Dadas las palabras en la revista y las palabras en la nota de rescate, escriba Sí si puede replicar su nota de rescate exactamente usando palabras completas de la revista; de lo contrario, imprima No.


// Basicamente este algoritmo es una implementación de una tabla de hash. 
// Se guardan las palabras y se cuenta cuantas repeticiones hay de cada una y se guardan en el arreglo hash.(map) 
// Luego se recorre la nota de rescate y se van restando las repeticiones de cada palabra en map.
// Si alguna palabra en map tiene una repetición negativa, entonces no se puede hacer la nota de rescate.
function ransomNote(magazine, note) {
	let itCan = true;
	let map = {};

	for (let word of magazine) {
		map[word] = (map[word] || 0) + 1;
		console.log(map);
	}

	console.log('-----------------------------');

	for (let word of note) {
		map[word] = (map[word] || 0) - 1;
		console.log(map);
	}

	for (let key in map) {
		if (map[key] < 0) {
			itCan = false;
			break;
		}
	}

	itCan && console.log('Yes');
	!itCan && console.log('No');
}

let magazine = ['give', 'one', 'grand', 'today', 'night', 'give'];
let note = ['give', 'one', 'grand', 'today'];

ransomNote(magazine, note);

// function ransomNote(magazine, note) {
//     let magazineHash = {};
//     let noteHash = {};

//     for (let i = 0; i < magazine.length; i++) {
//         if (magazineHash[magazine[i]]) {
//             magazineHash[magazine[i]]++;
//         } else {
//             magazineHash[magazine[i]] = 1;
//         }
//     }

//     for (let i = 0; i < note.length; i++) {
//         if (magazineHash[note[i]]) {
//             magazineHash[note[i]]--;
//         } else {
//             return false;
//         }
//     }

//     return true;
// }
