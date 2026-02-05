import { updateTaskStatus, deleteTask } from "../api/taskApi";

function TaskItem({ task, onUpdate }) {
  const handleStatusChange = async (newStatus) => {
    await updateTaskStatus(task._id, newStatus);
    onUpdate();
  };

  const handleDelete = async () => {
    await deleteTask(task._id);
    onUpdate();
  };

  return (
    <div className={`task-item ${task.status === "DONE" ? "done" : ""}`}>
      <div>
        <div className="task-title">{task.title}</div>

        <div
          className={`task-status ${
            task.status === "TODO"
              ? "status-todo"
              : task.status === "IN_PROGRESS"
              ? "status-progress"
              : "status-done"
          }`}
        >
          {task.status.replace("_", " ")}
        </div>
      </div>

      <div className="task-actions">
        {task.status === "TODO" && (
          <button
            className="btn-start"
            onClick={() => handleStatusChange("IN_PROGRESS")}
          >
            Start
          </button>
        )}

        {task.status === "IN_PROGRESS" && (
          <button
            className="btn-done"
            onClick={() => handleStatusChange("DONE")}
          >
            Done
          </button>
        )}

        <button className="btn-delete" onClick={handleDelete}>
          Delete
        </button>
      </div>
    </div>
  );
}

export default TaskItem;
