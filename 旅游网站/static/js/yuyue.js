// 导航栏链接点击事件
const navLinks = document.querySelectorAll('nav a');
const bookingSections = document.querySelectorAll('.booking-section');
navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const targetId = link.getAttribute('href').substring(1);
    bookingSections.forEach((section) => {
      section.style.display = 'none';
    });
    const targetSection = document.getElementById(targetId);
    if (targetSection) {
      targetSection.style.display = 'block';
    }
  });
});

function showTimeSelector(dateInput) {
    const timeSelector = document.getElementById('departureTime');
    if (dateInput.value) {
        timeSelector.style.display = 'block';
    } else {
        timeSelector.style.display = 'none';
    }
}


// 处理表单提交的函数
function handleFormSubmit(event) {
    event.preventDefault(); // 阻止表单默认提交行为
    const form = event.target;
    if (!form.checkValidity()) {
        alert('请填写所有必填项');
        return;
    }
    let formData = {};
    for (let i = 0; i < form.elements.length; i++) {
        const element = form.elements[i];
        if (element.name) {
            if (element.name === 'departureDate' && document.getElementById('departureTime').value) {
                formData[element.name] = element.value + ' ' + document.getElementById('departureTime').value;
            } else {
                formData[element.name] = element.value;
            }
        }
    }
    // 添加类型标识和唯一ID
    const type = form.dataset.type; // 假设您的表单有 data-type 属性
    formData.type = type;
    formData.id = Date.now(); // 使用时间戳作为唯一ID

    // 连接数据库并插入数据
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/save_booking', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
       if (xhr.readyState === 4 && xhr.status === 200) {
    Swal.fire({
        icon: 'success',
        title: '预约成功！',
        showConfirmButton: false,
        timer: 1500
    }).then(() => {
        location.reload();
    });
}
    };
    xhr.send(JSON.stringify(formData));
}

// 显示预订信息到表格中
function displayBookings() {
    const tables = {
        '酒店': document.getElementById('hotelBookingsTable').querySelector('tbody'),
        '机票': document.getElementById('flightBookingsTable').querySelector('tbody'),
        '旅游套餐': document.getElementById('packageBookingsTable').querySelector('tbody')
    };
    Object.values(tables).forEach(tbody => tbody.innerHTML = ''); // 清空现有数据

    // 从服务器获取最新数据
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_bookings', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const bookings = JSON.parse(xhr.responseText);
            bookings.forEach(booking => {
                const tableBody = tables[booking.type];
                if (tableBody) {
                    const row = document.createElement('tr');
                    Object.entries(booking).forEach(([key, value]) => {
                        const cell = document.createElement('td');
                        cell.textContent = value;
                        row.appendChild(cell);
                    });
                    const deleteCell = document.createElement('td');
                    const deleteButton = document.createElement('button');
                    deleteButton.textContent = 'Delete';
                    deleteButton.onclick = function () {
                        deleteBooking(booking.id);
                    };
                    deleteCell.appendChild(deleteButton);
                    row.appendChild(deleteCell);
                    tableBody.appendChild(row);
                }
            });
        }
    };
    xhr.send();
}

function deleteBooking(id) {
    Swal.fire({
        title: '确定要删除该订单吗？',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '确认删除'
    }).then((result) => {
        if (result.isConfirmed) {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/delete_booking', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200 && xhr.responseText === 'Success') {
                        Swal.fire(
                            '删除成功！',
                            '订单已被成功删除。',
                            'success'
                        ).then(() => {
                            location.reload();
                        });
                    } else {
                        Swal.fire(
                            '删除失败',
                            '原因：' + xhr.responseText,
                            'error'
                        );
                    }
                }
            };
            xhr.send(JSON.stringify({id: id}));
        }
    });
}

// 监听表单提交按钮点击事件
document.addEventListener('DOMContentLoaded', function() {
    // 处理“Show More”按钮点击事件
    const moreInfoButtons = document.querySelectorAll('.more-info-button');
    moreInfoButtons.forEach(button => {
        button.addEventListener('click', function() {
            const moreInfoDiv = this.nextElementSibling;
            if (moreInfoDiv.style.display === 'none') {
                moreInfoDiv.style.display = 'block';
                this.textContent = 'Show Less';
            } else {
                moreInfoDiv.style.display = 'none';
                this.textContent = 'Show More';
            }
        });
    });

    // 处理删除订单按钮点击事件
    const hotelTable = document.getElementById('hotelBookingsTable');
    const flightTable = document.getElementById('flightBookingsTable');
    const packageTable = document.getElementById('packageBookingsTable');

    hotelTable.addEventListener('click', function (e) {
        if (e.target.tagName === 'BUTTON' && e.target.textContent === '删除订单') {
            const bookingId = e.target.closest('tr').dataset.bookingId;
            deleteBooking(bookingId);
        }
    });

    flightTable.addEventListener('click', function (e) {
        if (e.target.tagName === 'BUTTON' && e.target.textContent === '删除订单') {
            const bookingId = e.target.closest('tr').dataset.bookingId;
            deleteBooking(bookingId);
        }
    });

    packageTable.addEventListener('click', function (e) {
        if (e.target.tagName === 'BUTTON' && e.target.textContent === '删除订单') {
            const bookingId = e.target.closest('tr').dataset.bookingId;
            deleteBooking(bookingId);
        }
    });
});