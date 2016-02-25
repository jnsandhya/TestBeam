#ifndef DataFormats_ForwardDetId_HGCalTBDetId_H
#define DataFormats_ForwardDetId_HGCalTBDetId_H 1

#include <iosfwd>
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/ForwardDetId/interface/ForwardSubdetector.h"

/* This class is bit-compatible with HGCalDetId, but is better-matched to the testbeams.

   On a sensor, the indexes are X and V.  X is horizontal (in most diagrams) and V increases along the hexagon faces towards the upper right.

 */
class HGCalTBDetId : public DetId {

public:
  static const int kHGCalTBXOffset       = 0;
  static const int kHGCalTBXMask         = 0xFF;
  static const int kHGCalTBVOffset       = 8;
  static const int kHGCalTBVMask         = 0xFF;
  static const int kHGCalTBSensorOffset  = 16;
  static const int kHGCalTBSensorMask    = 0x7F;
  static const int kHGCalTBCalibFlagOffset = 23;
  static const int kHGCalTBCalibFlagMask = 0x1;
  static const int kHGCalLayerOffset     = 24;
  static const int kHGCalLayerMask       = 0x7F;
  static const int kHGCalZsideOffset     = 31;
  static const int kHGCalZsideMask       = 0x1;

  /** Create a null cellid*/
  HGCalTBDetId();
  /** Create cellid from raw id (0=invalid tower id) */
  HGCalTBDetId(uint32_t rawid);
  /** Constructor from layer, sensor, ix, iv, calibr cell numbers */
  HGCalTBDetId(int lay, int sensor, int ix, int iv, bool isCalib=false);
  /** Constructor from a generic cell id */
  HGCalTBDetId(const DetId& id);
  /** Assignment from a generic cell id */
  HGCalTBDetId& operator=(const DetId& id);

  /// get the absolute value of the cell #'s
  int ix() const { return int8_t(id_&kHGCalTBXMask); }
  int iv() const { return int8_t((id_>>kHGCalTBVOffset)&kHGCalTBVMask); }

  /// get the sensor #
  int sensor() const { return (id_>>kHGCalTBSensorOffset)&kHGCalTBSensorMask; }

  /// is this a calibration channel?
  bool isCalib() const { return ( (id_>>kHGCalTBCalibFlagOffset)&kHGCalTBCalibFlagMask); }

  /// get the layer #
  int layer() const { return (id_>>kHGCalLayerOffset)&kHGCalLayerMask; }

  /// get the z-side of the cell (1/-1)
  int zside() const { return ((id_>>kHGCalZsideOffset) & kHGCalZsideMask ? 1 : -1); }

  /// consistency check : no bits left => no overhead
  bool isHGCal()   const { return true; }
  bool isForward() const { return true; }

};

std::ostream& operator<<(std::ostream&,const HGCalTBDetId& id);

#endif