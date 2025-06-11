def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  # sort by profit
    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline
    result = []

    for job_id, deadline, profit in jobs:
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job_id
                result.append(job_id)
                break
    return result

if __name__ == "__main__":
    jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    print("Scheduled jobs:", job_sequencing(jobs))

