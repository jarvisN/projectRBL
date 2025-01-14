import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './DataTable.css'; 

const DataTable = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [count, setCount] = useState(0); // เพิ่ม State สำหรับเก็บค่า Count
  useEffect(() => {
    axios.get('http://192.168.3.13:8000/log')
      .then(response => {
        setData(response.data.data);
        setCount(response.data.data.length); // ตั้งค่าค่า Count
      })
      .catch(error => {
        console.error('เกิดข้อผิดพลาดในการดึงข้อมูล:', error);
        setError(error.message);
      });
  }, []);

  if (error) {
    return <div>Error_test: {error}</div>;
  }

  return (
    <div>
      <h2>TABLE</h2>
      <p>Count of Class: {10 - count}</p>
      <table className="table-container"> {/* เพิ่ม className เพื่อใช้งาน CSS */}
        <thead>
          <tr>
            <th>Date</th>
            <th>Nickname</th>
            <th>Course</th>
            {/* เพิ่มหัวข้อตารางเพิ่มเติมตามความต้องการ */}
          </tr>
        </thead>
        <tbody>
          {data.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.column1}</td>
              <td>{item.column2}</td>
              {/* <td>{item.column3 || 'N/A' }</td> */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;



// import React, { useEffect, useState } from 'react';
// import axios from 'axios';
// import './DataTable.css';


// const DataTable = () => {
//   const [data, setData] = useState([]);
//   const [error, setError] = useState(null);
//   const [count, setCount] = useState(0); // เพิ่ม State สำหรับเก็บค่า Count
//   useEffect(() => {
//     axios.get('http://192.168.3.13:8000/log')
//       .then(response => {
//         setData(response.data.data);
//         setCount(response.data.data.length); // ตั้งค่าค่า Count
//       })
//       .catch(error => {
//         console.error('เกิดข้อผิดพลาดในการดึงข้อมูล:', error);
//         setError(error.message);
//       });
//   }, []);

//   if (error) {
//     return <div>Error_test: {error}</div>;
//   }

//   return (
//     <div>
//       <h2>TABLE</h2>
//       <p>Count of Class: {10 - count}</p>
//       <table>
//         <thead>
//           <tr>
            
//             <th>Date</th>
//             <th>Nickname</th>
//             <th>Course</th>
//             {/* เพิ่มหัวข้อตารางเพิ่มเติมตามความต้องการ */}
//           </tr>
//         </thead>
//         <tbody>
//           {data.map(item => (
//             <tr key={item.id}>
    
//               <td>{item.id}</td>
//               <td>{item.column1}</td>
//               <td>{item.column2}</td>
//               {/* <td>{item.column3 || 'N/A' }</td> */}
//             </tr>
            
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// export default DataTable;