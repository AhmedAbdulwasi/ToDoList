import React, {useState} from "react";
import '../App.css';

const TasksForm = ({ fetchTasks }) => {
  const [subject, setSubject] = useState("")
  const [description, setDescription] = useState("")
  const [completed, setCompleted] = useState(false)
  const [date, setDate] = useState("")

  const onSubmit = async (e) => {
    e.preventDefault() 

    const data = { subject, description, completed, date }
    const url = "http://127.0.0.1:5000/api/createtasks"
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    }
    const response = await fetch(url, options)
    if (response.status !== 200 && response.status !== 201) {
      const msg = await response.json()
      alert(msg.message)
    } else {
      alert("Task created successfully!")
      fetchTasks() 
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <div className="tasksform">
        <label htmlFor="subject">Subject: </label>
        <input
          type="text"
          id="subject"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
        />

        <label htmlFor="description">Description: </label>
        <input
          type="text"
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <label htmlFor="completed">Completed? </label>
        <input
          type="checkbox"
          id="completed"
          checked={completed}
          onChange={(e) => setCompleted(e.target.checked)}
        />

        <label htmlFor="date">Date: </label>
        <input
          type="datetime-local"
          id="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </div>
      <button type="submit">Create A Task</button>
    </form>
  )
}

export default TasksForm;