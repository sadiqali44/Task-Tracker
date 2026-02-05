import { useEffect, useState } from "react";
import { getTasks } from "./api/taskApi";
import TaskList from "./components/TaskList";
import TaskForm from "./components/TaskForm";

function App() {
  const [tasks, setTasks] = useState([]);
  const [showModal, setShowModal] = useState(false);

  const fetchTasks = async () => {
    const data = await getTasks();
    setTasks(data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="app">
      <h1>Task Tracker</h1>

      <button className="add-btn" onClick={() => setShowModal(true)}>
        + Add Task
      </button>

      <TaskList tasks={tasks} onUpdate={fetchTasks} />

      {showModal && (
        <TaskForm
          onTaskCreated={() => {
            fetchTasks();
            setShowModal(false);
          }}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
}

export default App;
