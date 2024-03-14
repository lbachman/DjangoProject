﻿using System;
using System.Collections.Generic;

namespace Pratice2.AttendanceModels;

public partial class User
{
    public uint UserId { get; set; }

    public string UserName { get; set; } = null!;

    public virtual ICollection<Class> Classes { get; set; } = new List<Class>();
}
