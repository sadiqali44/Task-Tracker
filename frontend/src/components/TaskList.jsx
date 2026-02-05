import TaskItem from "./TaskItem";

function TaskList({ tasks, onUpdate }) {
  return (
    <div>
      {tasks.map((task) => (
        <TaskItem
          key={task._id}        // ✅ FIX HERE
          task={task}
          onUpdate={onUpdate}
        />
      ))}
    </div>
  );
}

export default TaskList;
