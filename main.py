import random, time
import tabulate

#THIS PARTITION FUNCTION IS ADAPTED ENTIRELY FROM THE LECTURE
def partition(a, low, high, pivot_fn):
    pivot_index = pivot_fn(a, low, high)
    pivot = a[pivot_index]
    a[pivot_index], a[high] = a[high], a[pivot_index]
    i = low
    for j in range(low, high):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[high] = a[high], a[i]
    return i
#LECTURE CODE ENDS HERE

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + selection_sort(L[1:])
        
def qsort(a, pivot_fn, low = 0, high = None):

    if high is None:
        #We leave high to be an optional parameter, setting it as the idx of the last element
        high = len(a) - 1
    
    if low < high: #We must make sure this is the case before we perform any operation
        
        #Partition our array a accordingly
        part = partition(
            a, low, high, pivot_fn
        )
        
        #Now, we can send both parts to qsort
        qsort(a, pivot_fn, low, part - 1)
        qsort(a, pivot_fn, part + 1, high)
        #This is reminiscent of binary search
    
    return a

#This function is the case that we use the first element as the pivot
def first_pivot(a, low, high):
    return low #low is idx of the first element

#Case 2 -> We have a random pivot
def rand_pivot(a, low, high):
    return random.randint(low, high)

    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda l: qsort(l, first_pivot)
    qsort_random_pivot = lambda l: qsort(l, rand_pivot) #Using lambda function, we test qsort with different pivots
    tim_sort = sorted #Since this is built in into python
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)

        #Implemented the tests for all our sorting algos
        result.append([
            size,
            time_search(qsort_fixed_pivot, mylist.copy()),
            time_search(qsort_random_pivot, mylist.copy()),
            time_search(tim_sort, mylist.copy())
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    
    print(tabulate.tabulate(results,
        headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim_sort'],
        floatfmt=".3f",
        tablefmt="github"))


def test_print():
    print_results(compare_sort())

random.seed()
test_print()

'''
Using random permutations
------------------------
|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|--------|---------------------|----------------------|------------|
|    100 |               0.111 |                0.140 |      0.009 |
|    200 |               0.214 |                0.283 |      0.017 |
|    500 |               0.633 |                0.855 |      0.046 |
|   1000 |               1.395 |                2.017 |      0.100 |
|   2000 |               3.092 |                3.870 |      0.233 |
|   5000 |               8.394 |               10.649 |      0.605 |
|  10000 |              18.453 |               22.178 |      1.280 |
|  20000 |              38.971 |               48.260 |      2.905 |
|  50000 |             107.383 |              128.790 |      7.811 |
| 100000 |             220.212 |              285.027 |     16.898 |
'''


'''
Using pre-sorted lists
'''