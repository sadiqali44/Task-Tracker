const BASE_URL = "http://127.0.0.1:8000/api/tasks";

// Get all tasks
export const getTasks = async () => {
  const response = await fetch(`${BASE_URL}/all/`);
  return response.json();
};

// Create a new task
export const createTask = async (title) => {
  const response = await fetch(`${BASE_URL}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });

  return response.json();
};

// Update task status
export const updateTaskStatus = async (id, status) => {
  const response = await fetch(`${BASE_URL}/${id}/`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ status }),
  });

  return response.json();
};

// Delete task (bonus)
export const deleteTask = async (id) => {
  const response = await fetch(`${BASE_URL}/${id}/delete/`, {
    method: "DELETE",
  });

  return response.json();
};
