import React, {useState} from "react";
import "../App.css";

const TasksList = ({ tasks, fetchTasks }) => {
  const [editingTask, setEditingTask] = useState(null)
  const [editingData, setEditingData] = useState({
    subject: "",
    description: "",
    completed: false,
    date: ""
  })

  const deleteTask = async (taskId) => {
    const url = `http://127.0.0.1:5000/api/deletetasks/${taskId}`
    const options = {
      method: "DELETE",
    }
    const response = await fetch(url, options)
    if (response.status !== 200 && response.status !== 201) {
      const msg = await response.json()
      alert(msg.message)
    } else {
      alert("Task deleted successfully!")
      fetchTasks() 
    }
  }

  const handleEditClick = (task) => {
    setEditingTask(task.id)
    setEditingData({
      subject: task.subject,
      description: task.description,
      completed: task.completed,
      date: task.date
    })
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setEditingData({ ...editingData, [name]: value })
  }

  const handleCheckboxChange = (e) => {
    setEditingData({ ...editingData, completed: e.target.checked })
  }

  const handleUpdateSubmit = async (e) => {
    e.preventDefault()
    const { subject, description, completed, date } = editingData
    const url = `http://127.0.0.1:5000/api/updatetasks/${editingTask}`
    const options = {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ subject, description, completed, date })
    }
    const response = await fetch(url, options)
    if (response.status !== 200 && response.status !== 201) {
      const msg = await response.json()
      alert(msg.message)
    } else {
      alert("Task updated successfully!")
      fetchTasks() // Refresh tasks after update
      setEditingTask(null)
    }
  }

  return (
    <div className="taskslist">
      <h2>List of Tasks</h2>
      <table>
        <thead>
          <tr>
            <th>Subject</th>
            <th>Description</th>
            <th>Date</th>
            <th>Completed</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map((task) => (
            <tr key={task.id}>
              <td>{task.subject}</td>
              <td>{task.description}</td>
              <td>{task.date}</td>
              <td>{task.completed ? "Yes" : "No"}</td>
              <td>
                <button onClick={() => handleEditClick(task)}>Update</button>
                <button onClick={() => deleteTask(task.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {editingTask !== null && (
        <form onSubmit={handleUpdateSubmit}>
          <div>
            <label htmlFor="subject">Subject: </label>
            <input
              type="text"
              id="subject"
              name="subject"
              value={editingData.subject}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="description">Description: </label>
            <input
              type="text"
              id="description"
              name="description"
              value={editingData.description}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label htmlFor="completed">Completed? </label>
            <input
              type="checkbox"
              id="completed"
              name="completed"
              checked={editingData.completed}
              onChange={handleCheckboxChange}
            />
          </div>
          <div>
            <label htmlFor="date">Date: </label>
            <input
              type="datetime-local"
              id="date"
              name="date"
              value={editingData.date}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Update Task</button>
        </form>
      )}
    </div>
  )
}

export default TasksList;