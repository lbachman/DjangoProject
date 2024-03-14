using System;
using System.Collections.Generic;

namespace Pratice2.AttendanceModels;

public partial class Communication
{
    public uint ComId { get; set; }

    public uint InstructorId { get; set; }

    public string StudentUuid { get; set; } = null!;

    public uint ClassId { get; set; }

    public uint MessageId { get; set; }

    public virtual Message Message { get; set; } = null!;
}
