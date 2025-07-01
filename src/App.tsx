import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';

function App() {
  const [bots, setBots] = useState<any[]>([]);
  const [botName, setBotName] = useState('');
  const [bookingUrl, setBookingUrl] = useState('');
  const [selectedDate, setSelectedDate] = useState('');
  const [selectedCourt, setSelectedCourt] = useState('');
  const [playerName, setPlayerName] = useState('');
  const [playerEmail, setPlayerEmail] = useState('');

  // Create bot
  const createBot = async () => {
    if (!botName) return;
    
    const response = await fetch(`http://localhost:8000/bots?name=${encodeURIComponent(botName)}`, {
      method: 'POST'
    });
    
    if (response.ok) {
      const bot = await response.json();
      setBots([...bots, bot]);
      setBotName('');
    }
  };

  // Start monitoring
  const startMonitoring = async () => {
    if (!bookingUrl) return;
    
    const response = await fetch('http://localhost:8000/monitor', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: bookingUrl })
    });
    
    if (response.ok) {
      alert('Monitoring started successfully');
      setBookingUrl('');
    }
  };

  // Manual booking flow
  const startManualBooking = async () => {
    if (!bookingUrl || !selectedDate || !selectedCourt || !playerName || !playerEmail) {
      alert('Please fill in all booking details');
      return;
    }
    
    const response = await fetch('http://localhost:8000/book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        url: bookingUrl,
        date: selectedDate,
        court: selectedCourt,
        playerName,
        playerEmail
      })
    });
    
    if (response.ok) {
      const result = await response.json();
      alert(`Booking started: ${result.id}`);
      setSelectedDate('');
      setSelectedCourt('');
      setPlayerName('');
      setPlayerEmail('');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <h1 className="text-3xl font-bold">Tennis Court Booking Bot</h1>
        
        {/* Bot Configuration */}
        <Card className="p-6">
          <h2 className="text-xl font-semibold mb-4">Bot Configuration</h2>
          <div className="flex gap-2">
            <Input
              placeholder="Bot name"
              value={botName}
              onChange={(e) => setBotName(e.target.value)}
            />
            <Button onClick={createBot}>Create Bot</Button>
          </div>
          
          {/* Bot List */}
          <div className="mt-4 space-y-2">
            {bots.map((bot) => (
              <div key={bot.id} className="p-2 bg-gray-100 rounded">
                {bot.name}
              </div>
            ))}
          </div>
        </Card>

        {/* Court Monitoring */}
        <Card className="p-6">
          <h2 className="text-xl font-semibold mb-4">Court Monitoring</h2>
          <div className="flex gap-2">
            <Input
              placeholder="Booking website URL"
              value={bookingUrl}
              onChange={(e) => setBookingUrl(e.target.value)}
            />
            <Button onClick={startMonitoring} disabled={!bookingUrl}>
              Start Monitoring
            </Button>
          </div>
        </Card>

        {/* Manual Booking Flow */}
        <Card className="p-6">
          <h2 className="text-xl font-semibold mb-4">Manual Booking Flow</h2>
          <div className="space-y-4">
            <Input
              placeholder="Booking website URL"
              value={bookingUrl}
              onChange={(e) => setBookingUrl(e.target.value)}
            />
            <div className="grid grid-cols-2 gap-2">
              <Input
                type="date"
                placeholder="Select date"
                value={selectedDate}
                onChange={(e) => setSelectedDate(e.target.value)}
              />
              <Input
                placeholder="Court number/name"
                value={selectedCourt}
                onChange={(e) => setSelectedCourt(e.target.value)}
              />
            </div>
            <div className="grid grid-cols-2 gap-2">
              <Input
                placeholder="Player name"
                value={playerName}
                onChange={(e) => setPlayerName(e.target.value)}
              />
              <Input
                type="email"
                placeholder="Player email"
                value={playerEmail}
                onChange={(e) => setPlayerEmail(e.target.value)}
              />
            </div>
            <Button onClick={startManualBooking} className="w-full">
              Start Booking Process
            </Button>
          </div>
        </Card>
      </div>
    </div>
  );
}

export default App;