//Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

// Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
// First Element: firstElement, where firstElement is the first element in the sorted array.
// Last Element: lastElement, where lastElement is the last element in the sorted array.

// Dada una matriz de enteros, ordene la matriz en orden ascendente utilizando el algoritmo Bubble Sort anterior. Una vez ordenado, imprima las siguientes tres líneas:

// La matriz se ordena en numSwaps swaps., donde numSwaps es el número de intercambios que tuvieron lugar.
// Primer Elemento: primerElemento, donde primerElemento es el primer elemento en la matriz ordenada.
// Último elemento: último elemento, donde último elemento es el último elemento de la matriz ordenada.

function bubbleSort(a) {
  let numSwaps = 0;
  let swap = 0;

  for(let j=0; j<a.length; j++) {
    for (let i = 0; i < a.length - 1; i++) {
      if(a[i] > a[i + 1]) {
        numSwaps += 1;
        swap = a[i];
        a[i] = a[i + 1];
        a[i + 1] = swap;
      }
    }
  }
  
  console.log(`Array is sorted in ${numSwaps} swaps.`)
  console.log(`First Element: ${a[0]}`)
  console.log(`Last Element: ${a[a.length-1]}`)

  // return unorderedArray
}

bubbleSort([4, 6, 7, 1])
