import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [events, setEvents] = useState([]);

  const fetchEvents = async () => {
    try {
      const res = await axios.get('http://localhost:5000/webhook/events', {
        withCredentials: true,
      });
      setEvents((prev)=>[...res.data,...prev]);
    } catch (err) {
      console.error('Error fetching events:', err);
    }
  };

  useEffect(() => {
    fetchEvents(); // Initial fetch
    const interval = setInterval(fetchEvents, 15000); // Poll every 15 seconds
    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h2>GitHub Webhook Events</h2>
      <ul>
        {events.length === 0 ? (
          <p>No events yet.</p>
        ) : (
          events.map((e, i) => (
            <li key={i} style={{ marginBottom: '1rem' }}>
              <strong>{e.message}</strong><br />
              <span style={{ color: 'gray' }}>{new Date(e.timestamp).toLocaleString()}</span>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;
