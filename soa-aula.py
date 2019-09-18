process_queue = []
total_wtime = 0
n = int(input('Entrar com o número total de processos: '))
for i in range(n):
    process_queue.append([])
    process_queue[i].append(input('Entrar com o nome do processo: '))
    process_queue[i].append(int(input('Entrar p_chegada: ')))
    total_wtime += process_queue[i][1]
    process_queue[i].append(int(input('Entrar com p_burst: ')))
    print()
    
process_queue.sort(key = lambda process_queue:process_queue[1])

print('NomeProcesso\tHoraChegada\tTempoBurst')
for i in range(n):
    print(process_queue[i][0], '\t\t' ,process_queue[i][1], '\t\t' ,process_queue[i][2])
    
print('Tempo total de espera: ', total_wtime)
print('Tempo médio de espera: ',(total_wtime/n))