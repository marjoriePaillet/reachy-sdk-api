// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: orbita_kinematics.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Reachy.Sdk.Kinematics {

  /// <summary>Holder for reflection information generated from orbita_kinematics.proto</summary>
  public static partial class OrbitaKinematicsReflection {

    #region Descriptor
    /// <summary>File descriptor for orbita_kinematics.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static OrbitaKinematicsReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChdvcmJpdGFfa2luZW1hdGljcy5wcm90bxIVcmVhY2h5LnNkay5raW5lbWF0",
            "aWNzGhBraW5lbWF0aWNzLnByb3RvIjwKDE9yYml0YVRhcmdldBIsCgFxGAEg",
            "ASgLMiEucmVhY2h5LnNkay5raW5lbWF0aWNzLlF1YXRlcm5pb24iOAoKUXVh",
            "dGVybmlvbhIJCgF3GAEgASgBEgkKAXgYAiABKAESCQoBeRgDIAEoARIJCgF6",
            "GAQgASgBMnAKD09yYml0YUtpbmVtYXRpYxJdCg9Db21wdXRlT3JiaXRhSUsS",
            "Iy5yZWFjaHkuc2RrLmtpbmVtYXRpY3MuT3JiaXRhVGFyZ2V0GiUucmVhY2h5",
            "LnNkay5raW5lbWF0aWNzLkpvaW50c1Bvc2l0aW9uYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Reachy.Sdk.Kinematics.KinematicsReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Reachy.Sdk.Kinematics.OrbitaTarget), global::Reachy.Sdk.Kinematics.OrbitaTarget.Parser, new[]{ "Q" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Reachy.Sdk.Kinematics.Quaternion), global::Reachy.Sdk.Kinematics.Quaternion.Parser, new[]{ "W", "X", "Y", "Z" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class OrbitaTarget : pb::IMessage<OrbitaTarget>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<OrbitaTarget> _parser = new pb::MessageParser<OrbitaTarget>(() => new OrbitaTarget());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<OrbitaTarget> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reachy.Sdk.Kinematics.OrbitaKinematicsReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public OrbitaTarget() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public OrbitaTarget(OrbitaTarget other) : this() {
      q_ = other.q_ != null ? other.q_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public OrbitaTarget Clone() {
      return new OrbitaTarget(this);
    }

    /// <summary>Field number for the "q" field.</summary>
    public const int QFieldNumber = 1;
    private global::Reachy.Sdk.Kinematics.Quaternion q_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Reachy.Sdk.Kinematics.Quaternion Q {
      get { return q_; }
      set {
        q_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as OrbitaTarget);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(OrbitaTarget other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(Q, other.Q)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (q_ != null) hash ^= Q.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (q_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(Q);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (q_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(Q);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (q_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Q);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(OrbitaTarget other) {
      if (other == null) {
        return;
      }
      if (other.q_ != null) {
        if (q_ == null) {
          Q = new global::Reachy.Sdk.Kinematics.Quaternion();
        }
        Q.MergeFrom(other.Q);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (q_ == null) {
              Q = new global::Reachy.Sdk.Kinematics.Quaternion();
            }
            input.ReadMessage(Q);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (q_ == null) {
              Q = new global::Reachy.Sdk.Kinematics.Quaternion();
            }
            input.ReadMessage(Q);
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class Quaternion : pb::IMessage<Quaternion>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<Quaternion> _parser = new pb::MessageParser<Quaternion>(() => new Quaternion());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<Quaternion> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Reachy.Sdk.Kinematics.OrbitaKinematicsReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Quaternion() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Quaternion(Quaternion other) : this() {
      w_ = other.w_;
      x_ = other.x_;
      y_ = other.y_;
      z_ = other.z_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public Quaternion Clone() {
      return new Quaternion(this);
    }

    /// <summary>Field number for the "w" field.</summary>
    public const int WFieldNumber = 1;
    private double w_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double W {
      get { return w_; }
      set {
        w_ = value;
      }
    }

    /// <summary>Field number for the "x" field.</summary>
    public const int XFieldNumber = 2;
    private double x_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double X {
      get { return x_; }
      set {
        x_ = value;
      }
    }

    /// <summary>Field number for the "y" field.</summary>
    public const int YFieldNumber = 3;
    private double y_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double Y {
      get { return y_; }
      set {
        y_ = value;
      }
    }

    /// <summary>Field number for the "z" field.</summary>
    public const int ZFieldNumber = 4;
    private double z_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public double Z {
      get { return z_; }
      set {
        z_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as Quaternion);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(Quaternion other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(W, other.W)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(X, other.X)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Y, other.Y)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(Z, other.Z)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (W != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(W);
      if (X != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(X);
      if (Y != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Y);
      if (Z != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(Z);
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (W != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(W);
      }
      if (X != 0D) {
        output.WriteRawTag(17);
        output.WriteDouble(X);
      }
      if (Y != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(Y);
      }
      if (Z != 0D) {
        output.WriteRawTag(33);
        output.WriteDouble(Z);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (W != 0D) {
        output.WriteRawTag(9);
        output.WriteDouble(W);
      }
      if (X != 0D) {
        output.WriteRawTag(17);
        output.WriteDouble(X);
      }
      if (Y != 0D) {
        output.WriteRawTag(25);
        output.WriteDouble(Y);
      }
      if (Z != 0D) {
        output.WriteRawTag(33);
        output.WriteDouble(Z);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (W != 0D) {
        size += 1 + 8;
      }
      if (X != 0D) {
        size += 1 + 8;
      }
      if (Y != 0D) {
        size += 1 + 8;
      }
      if (Z != 0D) {
        size += 1 + 8;
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(Quaternion other) {
      if (other == null) {
        return;
      }
      if (other.W != 0D) {
        W = other.W;
      }
      if (other.X != 0D) {
        X = other.X;
      }
      if (other.Y != 0D) {
        Y = other.Y;
      }
      if (other.Z != 0D) {
        Z = other.Z;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 9: {
            W = input.ReadDouble();
            break;
          }
          case 17: {
            X = input.ReadDouble();
            break;
          }
          case 25: {
            Y = input.ReadDouble();
            break;
          }
          case 33: {
            Z = input.ReadDouble();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 9: {
            W = input.ReadDouble();
            break;
          }
          case 17: {
            X = input.ReadDouble();
            break;
          }
          case 25: {
            Y = input.ReadDouble();
            break;
          }
          case 33: {
            Z = input.ReadDouble();
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
