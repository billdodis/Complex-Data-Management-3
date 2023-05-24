def sort(array):
    for i in range(len(array)):
        minimumScore = array[i][0]
        minimumScoreIndex = i
        for y in range(i, len(array)):
            if minimumScore > array[y][0]:
                minimumScore = array[y][0]
                minimumScoreIndex = y
        swappedIndex = array[i]
        array[i] = array[minimumScoreIndex]
        array[minimumScoreIndex] = swappedIndex
    return array


def printer(array, accesses):
    print('Number of sequential accesses= ' + str(accesses))
    array.reverse()
    for x in array:
        print(str(x[1]) + ': ' + str(x[0]))


with open('rnd.txt') as f:
    lines = f.readlines()
    R = [None] * len(lines)
    RlowerBoundScore = [None] * len(lines)
    RtotalScore = [None] * len(lines)
    for line in lines:
        line = line.split(" ")
        identifier = int(line[0])
        rating = float(line[1])
        R[identifier] = rating

while True:
    try:
        k = int(input('Please give a positive integer, indicating how many top items will be included in the search: '))
    except ValueError:
        print("Wrong Input! This is not an integer!")
        continue
    else:
        if k < 0:
            print('Wrong Input! This is not a positive number!')
        else:
            break

with open('seq1.txt', 'r') as seq1, open('seq2.txt', 'r') as seq2:
    sequentialAccessesCounter = 0
    heap = []
    seq1LastRating = 0
    seq2LastRating = 0
    flag = False
    for line1, line2 in zip(seq1, seq2):
        if sequentialAccessesCounter == k:
            flag = True
            heap = sort(heap)
        seq1line = line1.split(" ")
        identifier = int(seq1line[0])
        rating = float(seq1line[1])
        if RlowerBoundScore[identifier] is None:
            RlowerBoundScore[identifier] = R[identifier] + rating
            RlowerBoundScore[identifier] = round(RlowerBoundScore[identifier], 2)
            if not flag:
                heap.append([RlowerBoundScore[identifier], identifier])
            if sequentialAccessesCounter >= k:
                threshold = rating + 5 + seq2LastRating
                if threshold > heap[0][0]:
                    if RlowerBoundScore[identifier] > heap[0][0]:
                        heap[0][0] = RlowerBoundScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                else:
                    flagg = False
                    heapArray = [x[1] for x in heap]
                    for x in range(len(RlowerBoundScore)):
                        if RlowerBoundScore[x] is not None and x not in heapArray:
                            if RlowerBoundScore[x] + rating > RlowerBoundScore[heap[0][1]] + rating:
                                flagg = True
                                break
                        if flagg:
                            break
                    if RlowerBoundScore[identifier] > heap[0][0]:
                        heap[0][0] = RlowerBoundScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                    if not flagg:
                        sequentialAccessesCounter += 1
                        printer(heap, sequentialAccessesCounter)
                        exit()

        else:
            RtotalScore[identifier] = RlowerBoundScore[identifier] + rating
            RtotalScore[identifier] = round(RtotalScore[identifier], 2)
            if not flag:
                heap.append([RtotalScore[identifier], identifier])
            if sequentialAccessesCounter >= k:
                threshold = rating + 5 + seq2LastRating
                if threshold > heap[0][0]:
                    if RtotalScore[identifier] > heap[0][0]:
                        heap[0][0] = RtotalScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                else:
                    flagg = False
                    heapArray = [x[1] for x in heap]
                    for x in range(len(RlowerBoundScore)):
                        if RlowerBoundScore[x] is not None and x not in heapArray:
                            if RlowerBoundScore[x] + rating > RlowerBoundScore[heap[0][1]] + rating:
                                flagg = True
                                break
                        if flagg:
                            break
                    if RtotalScore[identifier] > heap[0][0]:
                        heap[0][0] = RtotalScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                    if not flagg:
                        sequentialAccessesCounter += 1
                        printer(heap, sequentialAccessesCounter)
                        exit()
        seq1LastRating = rating
        sequentialAccessesCounter += 1
        if sequentialAccessesCounter == k:
            flag = True
            heap = sort(heap)
        seq2line = line2.split(" ")
        identifier = int(seq2line[0])
        rating = float(seq2line[1])
        if RlowerBoundScore[identifier] is None:
            RlowerBoundScore[identifier] = R[identifier] + rating
            RlowerBoundScore[identifier] = round(RlowerBoundScore[identifier], 2)
            if not flag:
                heap.append([RlowerBoundScore[identifier], identifier])
            if sequentialAccessesCounter >= k:
                threshold = rating + 5 + seq1LastRating
                if threshold > heap[0][0]:
                    if RlowerBoundScore[identifier] > heap[0][0]:
                        heap[0][0] = RlowerBoundScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                else:
                    flagg = False
                    heapArray = [x[1] for x in heap]
                    for x in range(len(RlowerBoundScore)):
                        if RlowerBoundScore[x] is not None and x not in heapArray:
                            if RlowerBoundScore[x] + rating > heap[0][0]:
                                flagg = True
                                break
                        if flagg:
                            break
                    if RlowerBoundScore[identifier] > heap[0][0]:
                        heap[0][0] = RlowerBoundScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                    if not flagg:
                        sequentialAccessesCounter += 1
                        printer(heap, sequentialAccessesCounter)
                        exit()
        else:
            RtotalScore[identifier] = RlowerBoundScore[identifier] + rating
            RtotalScore[identifier] = round(RtotalScore[identifier], 2)
            if not flag:
                heap.append([RtotalScore[identifier], identifier])
            if sequentialAccessesCounter >= k:
                threshold = rating + 5 + seq1LastRating
                if threshold > heap[0][0]:
                    if RtotalScore[identifier] > heap[0][0]:
                        heap[0][0] = RtotalScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                else:
                    flagg = False
                    heapArray = [x[1] for x in heap]
                    for x in range(len(RlowerBoundScore)):
                        if RlowerBoundScore[x] is not None and x not in heapArray:
                            if RlowerBoundScore[x] + rating > heap[0][0]:
                                flagg = True
                                break
                        if flagg:
                            break
                    if RtotalScore[identifier] > heap[0][0]:
                        heap[0][0] = RtotalScore[identifier]
                        heap[0][1] = identifier
                        heap = sort(heap)
                    if not flagg:
                        sequentialAccessesCounter += 1
                        printer(heap, sequentialAccessesCounter)
                        exit()
        seq2LastRating = rating
        sequentialAccessesCounter += 1
