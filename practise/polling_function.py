'''Task 2: The Custom Polling Loop (Time/While Loops)
The Scenario: You trigger an async video rendering job via an API. 
The API returns {"status": "processing"} immediately. 
You need to wait for it to say {"status": "completed"}.

The Prompt: Write a function that simulates a polling loop. 
It should check the status (you can mock the status check) every 2 seconds. 
If the status isn't "completed" after 10 seconds, it should raise a TimeoutError.
'''

def check_current_status(attempt_count):
    if attempt_count < 3:
        return {"status": "In progress"}
    return {"status": "completed"}

def wait_for_job_completion(timeout=10, poll_interval=2):
    start_time = time.time()
    attempt = 0

    while time.time() - start_time < timeout:
        attempt += 1

        response = check_current_status(attempt)
        status = response.get("status")

        if status == "completed":
            print("job success")
        time.sleep(poll_interval)

    raise TimeoutError("job did not complete in time")

if __name__ = "__main__":
    wait_for_job_completion()