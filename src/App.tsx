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

  // Tennis court booking function
  const startTennisBooking = async () => {
    try {
      // Open the booking page in a new window/tab
      const bookingUrl = "https://app.acuityscheduling.com/schedule/88825638/appointment/15247850";
      const bookingWindow = window.open(bookingUrl, '_blank', 'width=1200,height=800');
      
      if (!bookingWindow) {
        alert('Please allow popups to use the booking feature');
        return;
      }

      // Wait for the page to load and then execute the booking script
      setTimeout(() => {
        try {
          // Execute the court selection script in the new window
          bookingWindow.eval(`
            (function() {
              const addressText = "Alexander Park, 409 Yorkshire Way, Belmont, CA 94002";
              const courtName = "Alexander Court #1";

              const containers = document.querySelectorAll('.select-calendar div');
              let targetButton = null;

              containers.forEach(container => {
                const label = container.querySelector('p');
                if (label && label.textContent.trim() === addressText) {
                  const courtItems = container.querySelectorAll('li');

                  courtItems.forEach(item => {
                    const paragraphs = item.querySelectorAll('p');
                    paragraphs.forEach(p => {
                      if (p.textContent.trim() === courtName) {
                        const button = item.querySelector('button');
                        if (button && button.textContent.trim() === "Select") {
                          targetButton = button;
                        }
                      }
                    });
                  });
                }
              });

              if (targetButton) {
                targetButton.click();
                console.log('Select button clicked successfully!');
              } else {
                console.warn('Button not found!');
              }
            })();
          `);
          
          alert('Booking script executed! Check the opened window for Alexander Court #1 selection.');
        } catch (error) {
          console.error('Error executing booking script:', error);
          alert('Could not execute booking script due to security restrictions. Please manually select Alexander Court #1.');
        }
      }, 3000); // Wait 3 seconds for page to load
      
    } catch (error) {
      console.error('Error starting tennis booking:', error);
      alert('Error starting booking process');
    }
  };

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

        {/* Tennis Court Booking */}
        <Card className="p-6">
          <h2 className="text-xl font-semibold mb-4">Tennis Court Booking</h2>
          <p className="text-gray-600 mb-4">
            Automatically book Alexander Court #1 at Alexander Park
          </p>
          <Button onClick={startTennisBooking} className="w-full bg-green-600 hover:bg-green-700">
            Start Booking
          </Button>
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