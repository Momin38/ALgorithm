# Make a fuction of name insertionSort which take a argument wich is an arry
# An insertion sort is a way of sorting objects, like sorting a deck of cards.
# You start with unsorted cards in your right hand, and your left hand is empty.
# You take the first card from your right hand and move it to your left; The first card is now considered sorted.
# Next, you choose a second card from your right hand and compare it to the card in your left hand.
# now thier is two conditions for now is right hand side card is greater than left side or less than 
# if right hand side card is less than left side card then put it back to card which is alredy present in the left side hand 
#similarly you have two sorted cards Now take third card from right hand side 
# now you have a three condition first is greater second is mid and third is lesser
# put the cards accoring to its value 
# similary insertion sort is working 
# lets see code

'''
Algorithm 

insertionSort(arry):
    for i=1 to lenght for the arry
    key = arry[i]
    isert arry[i] into sorted sequence a[j...i+1]
    j = i-1
    while (j>=0 and a[j]>key)
        arry[j+1]= arry[j]
        j=j-1
    arry[j+1] =key
'''




def insertionSort(arr):
    for i in range(1,len(arr)):
        
        key = arr[i]            
        j = i-1   
        while (j>=0 and arr[j]>key):  
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        
    return arr
    
arry = [15,13,15,14,19,18,11,32,16]  
print('Unsorted arry is : ',arry)
print()
print('sorted arry is : ', insertionSort(arry))
            
