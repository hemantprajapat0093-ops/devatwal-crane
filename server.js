const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static frontend
app.use(express.static(path.join(__dirname, 'public')));

// Ensure data folder and storage files exist
const DATA_DIR = path.join(__dirname, 'data');
const BOOKINGS_FILE = path.join(DATA_DIR, 'bookings.json');
const CONTACTS_FILE = path.join(DATA_DIR, 'contacts.json');

if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}
if (!fs.existsSync(BOOKINGS_FILE)) {
  fs.writeFileSync(BOOKINGS_FILE, JSON.stringify([], null, 2));
}
if (!fs.existsSync(CONTACTS_FILE)) {
  fs.writeFileSync(CONTACTS_FILE, JSON.stringify([], null, 2));
}

// Mailer Setup (Configurable via ENV or Fallback mode)
const PRIMARY_OWNER_EMAIL = process.env.OWNER_EMAIL || 'satyapaldevatwal@gmail.com';
const PRIMARY_PHONE_1 = '9414333328';
const PRIMARY_PHONE_2 = '9950233073'; // Satyapal ji
const MAMAN_PHONE = '8003721244';
const DHARMINDER_PHONE = '9982842357';

let transporter = null;
if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
  transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT || '587'),
    secure: process.env.SMTP_SECURE === 'true',
    auth: {
      user: process.env.SMTP_USER,
      pass: process.env.SMTP_PASS,
    },
  });
}

// Helper: read and write JSON safely
function readJson(filePath) {
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(raw);
  } catch (err) {
    return [];
  }
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

// API: Create Booking
app.post('/api/bookings', async (req, res) => {
  try {
    const {
      name,
      phone,
      email,
      craneType,
      workType,
      date,
      timeSlot,
      location,
      pincode = '301705',
      loadWeight,
      notes,
    } = req.body;

    if (!name || !phone || !craneType || !workType) {
      return res.status(400).json({
        success: false,
        message: 'कृपया नाम, मोबाइल नंबर, क्रेन का प्रकार और काम का विवरण भरें (Please fill required fields).',
      });
    }

    const bookingId = 'DCS-' + Date.now().toString().slice(-6);
    const createdAt = new Date().toISOString();

    const newBooking = {
      id: bookingId,
      name,
      phone,
      email: email || 'N/A',
      craneType,
      workType,
      date: date || 'Immediate / 24x7 Call',
      timeSlot: timeSlot || 'Immediate / As Soon As Possible',
      location: location || 'RIICO Ghiloth / Neemrana Industrial Area',
      pincode: pincode || '301705',
      loadWeight: loadWeight || 'To be assessed on site',
      notes: notes || '',
      status: 'CONFIRMED_PENDING_DISPATCH',
      createdAt,
    };

    const bookings = readJson(BOOKINGS_FILE);
    bookings.unshift(newBooking);
    writeJson(BOOKINGS_FILE, bookings);

    // Prepare formatted text for WhatsApp and Email notifications
    const summaryText = `NEW CRANE BOOKING [${bookingId}]\n` +
      `----------------------------------------\n` +
      `Customer Name: ${name}\n` +
      `Phone Number: ${phone}\n` +
      `Email: ${email || 'Not provided'}\n` +
      `Crane Variety: ${craneType}\n` +
      `Work Type: ${workType}\n` +
      `Required Date: ${newBooking.date}\n` +
      `Time Slot: ${newBooking.timeSlot}\n` +
      `Location: ${newBooking.location} (Pincode: ${newBooking.pincode})\n` +
      `Estimated Load: ${newBooking.loadWeight}\n` +
      `Special Instructions: ${notes || 'None'}\n` +
      `Booking Time: ${new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })}\n` +
      `----------------------------------------\n` +
      `Devatwal Crane Service - 24/7 Available in 301705`;

    // Attempt SMTP Email if transporter exists
    let emailSent = false;
    if (transporter) {
      try {
        await transporter.sendMail({
          from: `"Devatwal Crane Service" <${process.env.SMTP_USER}>`,
          to: PRIMARY_OWNER_EMAIL,
          subject: `🚨 [NEW BOOKING ${bookingId}] ${workType} - ${name} (${phone})`,
          text: summaryText,
          html: `
            <div style="font-family: Arial, sans-serif; background-color: #0f172a; padding: 24px; color: #f8fafc;">
              <div style="background-color: #1e293b; border-top: 4px solid #f59e0b; border-radius: 8px; padding: 24px; max-width: 600px; margin: 0 auto;">
                <h2 style="color: #f59e0b; margin-top: 0;">🚜 Devatwal Crane Service - New Booking Alert</h2>
                <p style="font-size: 16px;">A new crane booking has been placed on the official website!</p>
                <table style="width: 100%; border-collapse: collapse; margin: 20px 0; color: #e2e8f0;">
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Booking ID:</td><td style="color: #f59e0b;">${bookingId}</td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Customer:</td><td>${name}</td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Phone:</td><td><a href="tel:${phone}" style="color: #38bdf8; text-decoration: none;">${phone}</a></td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Crane Variety:</td><td>${craneType}</td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Work Type:</td><td>${workType}</td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Date & Time:</td><td>${newBooking.date} | ${newBooking.timeSlot}</td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Location:</td><td>${newBooking.location} (PIN: ${newBooking.pincode})</td></tr>
                  <tr style="border-bottom: 1px solid #334155;"><td style="padding: 8px 0; font-weight: bold;">Load Weight:</td><td>${newBooking.loadWeight}</td></tr>
                  <tr><td style="padding: 8px 0; font-weight: bold;">Notes:</td><td>${notes || 'None'}</td></tr>
                </table>
                <div style="margin-top: 24px; text-align: center;">
                  <a href="tel:${phone}" style="background-color: #f59e0b; color: #000; padding: 12px 24px; border-radius: 6px; font-weight: bold; text-decoration: none; margin-right: 12px; display: inline-block;">Call Customer Now</a>
                  <a href="https://wa.me/91${phone}" style="background-color: #22c55e; color: #fff; padding: 12px 24px; border-radius: 6px; font-weight: bold; text-decoration: none; display: inline-block;">WhatsApp Customer</a>
                </div>
              </div>
            </div>
          `,
        });
        emailSent = true;
      } catch (err) {
        console.error('Email sending error:', err);
      }
    } else {
      console.log('--- NEW BOOKING RECEIVED (SIMULATED EMAIL DISPATCH) ---');
      console.log(summaryText);
      console.log('Destination Email:', PRIMARY_OWNER_EMAIL);
      console.log('------------------------------------------------------');
    }

    // Pre-encode WhatsApp & Mailto URL for direct user trigger
    const waText = encodeURIComponent(
      `*Devatwal Crane Service - New Booking Request*\n\n` +
      `*Booking ID:* ${bookingId}\n` +
      `*Name:* ${name}\n` +
      `*Phone:* ${phone}\n` +
      `*Crane:* ${craneType}\n` +
      `*Work:* ${workType}\n` +
      `*Date/Slot:* ${newBooking.date} (${newBooking.timeSlot})\n` +
      `*Location:* ${newBooking.location} (PIN: ${newBooking.pincode})\n` +
      `*Load:* ${newBooking.loadWeight}\n` +
      `*Details:* ${notes || 'Standard Service Required'}`
    );

    const mailSubject = encodeURIComponent(`Crane Booking Request [${bookingId}] - ${name}`);
    const mailBody = encodeURIComponent(
      `Hello Satyapal ji,\n\n` +
      `I have booked a crane via your website.\n\n` +
      `Booking Details:\n` +
      `- Booking ID: ${bookingId}\n` +
      `- Name: ${name}\n` +
      `- Phone: ${phone}\n` +
      `- Crane Variety: ${craneType}\n` +
      `- Work Required: ${workType}\n` +
      `- Date & Slot: ${newBooking.date} / ${newBooking.timeSlot}\n` +
      `- Location: ${newBooking.location} (PIN: ${newBooking.pincode})\n` +
      `- Estimated Load: ${newBooking.loadWeight}\n` +
      `- Notes: ${notes || 'None'}\n\n` +
      `Please confirm slot availability at the earliest.\n\n` +
      `Thank you,\n${name}`
    );

    res.json({
      success: true,
      bookingId,
      emailSent,
      ownerEmail: PRIMARY_OWNER_EMAIL,
      ownerPhones: [PRIMARY_PHONE_1, PRIMARY_PHONE_2],
      whatsappUrl: `https://wa.me/91${PRIMARY_PHONE_1}?text=${waText}`,
      mailtoUrl: `mailto:${PRIMARY_OWNER_EMAIL}?subject=${mailSubject}&body=${mailBody}`,
      booking: newBooking,
      message: 'आपकी बुकिंग सफलतापूर्वक दर्ज कर ली गई है! (Booking recorded successfully!)',
    });
  } catch (error) {
    console.error('Booking error:', error);
    res.status(500).json({ success: false, message: 'Server error processing booking.' });
  }
});

// API: Contact Message
app.post('/api/contact', (req, res) => {
  try {
    const { name, phone, email, subject, message } = req.body;
    if (!name || !phone || !message) {
      return res.status(400).json({ success: false, message: 'Missing required contact fields' });
    }

    const contacts = readJson(CONTACTS_FILE);
    const newContact = {
      id: 'MSG-' + Date.now().toString().slice(-6),
      name,
      phone,
      email: email || 'N/A',
      subject: subject || 'General Inquiry',
      message,
      createdAt: new Date().toISOString(),
    };
    contacts.unshift(newContact);
    writeJson(CONTACTS_FILE, contacts);

    console.log('--- NEW CONTACT MESSAGE ---');
    console.log(newContact);

    res.json({ success: true, message: 'संदेश प्राप्त हुआ! हमारी टीम जल्द ही आपसे संपर्क करेगी।' });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// API: Get Bookings (Recent)
app.get('/api/bookings', (req, res) => {
  const bookings = readJson(BOOKINGS_FILE);
  res.json({ success: true, total: bookings.length, bookings: bookings.slice(0, 50) });
});

// API: Health check
app.get('/api/health', (req, res) => {
  res.json({
    status: 'ONLINE',
    service: 'Devatwal Crane Service Web Portal',
    pincode: '301705',
    timing: '24/7 Round the clock',
    uptime: process.uptime(),
  });
});

// Wildcard route to serve index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`=======================================================`);
  console.log(`🚜 Devatwal Crane Service Portal running on port ${PORT}`);
  console.log(`📍 Location: RIICO Ghiloth, Neemrana, Alwar (301705)`);
  console.log(`📞 Direct Contact: Satyapal (+91 9414333328, 9950233073), Maman (+91 8003721244), Dharminder (+91 9982842357)`);
  console.log(`📧 Owner Email: ${PRIMARY_OWNER_EMAIL}`);
  console.log(`🌐 Local URL: http://localhost:${PORT}`);
  console.log(`=======================================================`);
});
