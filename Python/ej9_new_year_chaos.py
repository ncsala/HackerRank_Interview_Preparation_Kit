"""It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic."""


def minimumBribes(q):
    #Solution here
    
    q = [original_position-1 for original_position in q]  
    bribes = 0
    
    for after_bribes, original_position in enumerate(q):
        if original_position - after_bribes > 2:
            print("Too chaotic")     
            return
        #a continuacion revisamos quien recibio el soborno, no quien lo dio
        for possible_bribers in q[max(original_position - 1, 0):after_bribes]:
            if possible_bribers > original_position:
                bribes += 1

    print(bribes)

minimumBribes([1,2,4,5,6,7,8,3])    #[0, 1, 3, 4, 5, 6, 7, 2]